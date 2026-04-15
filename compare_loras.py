import os
import torch
import random
import warnings
from dotenv import load_dotenv
from transformers import logging as hf_logging
from diffusers import AutoPipelineForText2Image

load_dotenv()
warnings.filterwarnings("ignore", category=FutureWarning)
hf_logging.set_verbosity_error()

LORAS = [
    {"id": "ostris/watercolor_style_lora_sdxl", "trigger": "watercolor style, magical illustration"},
    {"id": "goofyai/Leonardo_Ai_Style_Illustration", "trigger": "pencil sketch and ink illustration"},
]

PROMPTS = [
    ("01_OCEAN_Visionary", "a female figure embodying the combination of visionary and creative, highly organized and disciplined, and charismatic and outgoing"),
    ("16_Ocean_Adaptable", "a male figure embodying the combination of visionary and creative, adaptable and spontaneous, and introspective and observant"),
    ("25_ocEAN_Tradition", "a female figure embodying the combination of practical and tradition-honoring, adaptable and spontaneous, and charismatic and outgoing"),
    ("06_OCeAn_Disciplined", "a male figure embodying the combination of visionary and creative, highly organized and disciplined, and introspective and observant")
]

class LoraComparer:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
        self.dtype = torch.float16 if self.device != "cpu" else torch.float32
        
        print(f"Loading SDXL Turbo Base Model on {self.device}...")
        self.pipeline = AutoPipelineForText2Image.from_pretrained(
            "stabilityai/sdxl-turbo",
            torch_dtype=self.dtype,
            variant="fp16" if self.device != "cpu" else None
        ).to(self.device)

    def run_comparisons(self):
        base_dir = "comparisons"
        os.makedirs(base_dir, exist_ok=True)
        
        for lora in LORAS:
            lora_id = lora["id"]
            trigger = lora["trigger"]
            safe_name = lora_id.split("/")[-1]
            
            lora_dir = os.path.join(base_dir, safe_name)
            os.makedirs(lora_dir, exist_ok=True)
            
            print(f"\n[{safe_name}] Testing LoRA...")
            
            try:
                # Load the unique style LoRA
                self.pipeline.load_lora_weights(lora_id, adapter_name="style")
                
                # Stack the Face Fixer LoRA
                face_lora = "Omarito2412/Rendered-Face-Detailer-SDXL"
                self.pipeline.load_lora_weights(face_lora, adapter_name="face_fix")
                
                # Combine them with specific weights
                self.pipeline.set_adapters(["style", "face_fix"], adapter_weights=[1.0, 0.7])
                
            except Exception as e:
                print(f"[{safe_name}] Error loading LoRA stack: {e}. Skipping.")
                continue
                
            for p_name, base_prompt in PROMPTS:
                seed = random.randint(0, 2147483647)
                generator = torch.Generator(device=self.device).manual_seed(seed)
                full_prompt = f"{trigger}, {base_prompt}"
                output_path = os.path.join(lora_dir, f"{p_name}_{seed}.png")
                
                print(f"  -> Generating {p_name} (seed: {seed})...", end=" ", flush=True)
                
                try:
                    image = self.pipeline(
                        prompt=full_prompt,
                        num_inference_steps=3,
                        guidance_scale=0.0,
                        generator=generator
                    ).images[0]
                    
                    image.save(output_path)
                    print("Done.")
                except Exception as e:
                    print(f"Failed. Error: {e}")
            
            print(f"[{safe_name}] Unloading LoRA weights to clear VRAM...")
            try:
                self.pipeline.unload_lora_weights()
            except Exception as e:
                print(f"[Warning] Could not cleanly unload LoRA: {e}")
                
        print("\nAll comparisons completed!")

if __name__ == "__main__":
    comparer = LoraComparer()
    comparer.run_comparisons()
