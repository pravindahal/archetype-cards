import os
import torch
import warnings
from dotenv import load_dotenv
from transformers import logging as hf_logging
from diffusers import AutoPipelineForText2Image

# Load local environment variables from .env
load_dotenv()

# Suppress noisy deprecation warnings from transformers
warnings.filterwarnings("ignore", category=FutureWarning)
hf_logging.set_verbosity_error()

class ArchetypeCardGenerator:
    """
    A local Python wrapper for generating archetype card art using SDXL Turbo and a Tarot LoRA.
    SDXL Turbo allows for blazing-fast 1-4 step generation locally.
    
    Prerequisites:
      pip install diffusers transformers accelerate invisible_watermark safetensors
    """
    def __init__(self):
        # Autodetect hardware (Mac M-series (mps), NVIDIA (cuda), or fallback to cpu)
        self.device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
        
        # CPU doesn't support fp16 operations in standard PyTorch easily
        self.dtype = torch.float16 if self.device != "cpu" else torch.float32
        
        print(f"Loading SDXL Turbo Base Model on {self.device}...")
        self.pipeline = AutoPipelineForText2Image.from_pretrained(
            "stabilityai/sdxl-turbo",
            torch_dtype=self.dtype,
            variant="fp16" if self.device != "cpu" else None
        ).to(self.device)
        
        print("Loading Hugging Face Tarot LoRA...")
        try:
            # multimodalart/tarot-z-image-lora is widely available and trained for SDXL 
            self.pipeline.load_lora_weights("multimodalart/tarot-z-image-lora")
            # Optionally fuse the weights for slightly faster inference:
            # self.pipeline.fuse_lora(lora_scale=1.0)
            print("LoRA successfully loaded!")
        except Exception as e:
            print(f"Warning: Could not load LoRA. Falling back to base model. Error: {e}")
            
    def generate(self, description, output_filename, steps=4, guidance_scale=0.0):
        """
        Generates an image.
        For SDXL Turbo:
        - steps must be low (1 to 4 is standard).
        - guidance_scale must be 0.0 to disable CFG (as Turbo models are distilled).
        """
        # "trtcrd" is the trigger word for this specific LoRA to force the tarot aesthetic
        # We append "tarot card style" just to strengthen it natively globally too.
        full_prompt = f"trtcrd tarot card style, {description}, intricate details, highly aesthetic, masterpiece"
        
        print(f"\nGenerating image...")
        print(f"Prompt: {full_prompt}")
        
        # Generate the image
        image = self.pipeline(
            prompt=full_prompt,
            num_inference_steps=steps, 
            guidance_scale=guidance_scale 
        ).images[0]
        
        # Save output
        os.makedirs("card_art", exist_ok=True)
        filepath = os.path.join("card_art", output_filename)
        image.save(filepath)
        print(f"Success! Image saved to: {filepath}")

if __name__ == "__main__":
    print("Initializing Archetype Generator...")
    generator = ArchetypeCardGenerator()
    
    # Let's test it out using one of our 32 configurations (OCEAN - The Passionate Champion)
    test_concept = "a charismatic and outgoing female figure carrying a glowing lantern through a swirling storm, organized and disciplined pose"
    test_filename = "01_OCEAN_art.png"
    
    generator.generate(
        description=test_concept,
        output_filename=test_filename,
        steps=4  # Kept extremely short per SDXL Turbo requirements
    )
