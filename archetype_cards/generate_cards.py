import os
import torch
import warnings
from dotenv import load_dotenv
from transformers import logging as hf_logging
from diffusers import Flux2KleinPipeline, Flux2Transformer2DModel, GGUFQuantizationConfig
from huggingface_hub import hf_hub_download

# Load local environment variables from .env
load_dotenv()

# Suppress noisy deprecation warnings from transformers
warnings.filterwarnings("ignore", category=FutureWarning)
hf_logging.set_verbosity_error()

class ArchetypeCardGenerator:
    """
    A local Python wrapper for generating archetype card art using FLUX.2 [klein] 4B Q6_K.
    FLUX.2 [klein] is a distilled model that produces high-quality results in 4 steps.
    
    Prerequisites:
      pip install -U diffusers transformers accelerate gguf huggingface_hub sentencepiece safetensors python-dotenv
    """
    def __init__(self):
        # Autodetect hardware (Mac M-series (mps), NVIDIA (cuda), or fallback to cpu)
        self.device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
        self.dtype = torch.bfloat16
        
        gguf_repo = "unsloth/FLUX.2-klein-4B-GGUF"
        gguf_file = "flux-2-klein-4b-Q6_K.gguf"
        base_model = "black-forest-labs/FLUX.2-klein-4B"
        
        print(f"Downloading/Loading {gguf_file} from {gguf_repo}...")
        ckpt_path = hf_hub_download(gguf_repo, gguf_file)
        
        print(f"Loading quantized Flux2Transformer2DModel (Q6_K GGUF)...")
        transformer = Flux2Transformer2DModel.from_single_file(
            ckpt_path,
            config=base_model,
            subfolder="transformer",
            quantization_config=GGUFQuantizationConfig(compute_dtype=self.dtype),
            torch_dtype=self.dtype,
        )
        
        print(f"Building Flux2KleinPipeline on {self.device}...")
        self.pipeline = Flux2KleinPipeline.from_pretrained(
            base_model,
            transformer=transformer,
            torch_dtype=self.dtype,
        ).to(self.device)
            
    def generate(self, description, output_filename, steps=4, guidance_scale=1.0):
        """
        Generates an image.
        For FLUX.2 [klein] distilled 4B:
        - steps: 4 is the sweet spot (distilled model).
        - guidance_scale: 1.0 is recommended for the distilled variant.
        """
        style_guide = """
            archival illustration style,
            heavy black outlines,
            occult aesthetic,
            symbolic allegory,
            central archetype,
            flattened perspective,
            rich saturated colors,
            limited color palette,
            aged parchment texture,
            mystical semiotics,
            intricate linework,
            dense patterns,
            hand-drawn quality,
            dramatic lighting,
            esoteric ambiance
        """
        full_prompt = f"{description}, {style_guide}"
        
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
    test_concept = """
    The artisan: A gentle, introspective female figure working meticulously on a beautiful, complex piece of art or illuminated manuscript in a quiet, dimly lit sanctuary. The soft, moody lighting reflects her solitary nature, deep emotional vigilance, and disciplined creativity.
    """
    test_filename = "05_OCEAN_art.png"
    
    generator.generate(
        description=test_concept,
        output_filename=test_filename,
        steps=4,  # Distilled FLUX.2 klein produces quality results in just 4 steps
        guidance_scale=1.0
    )
