import os
import magenta.music as mm
from magenta.models.music_vae import configs
from magenta.models.music_vae.trained_model import TrainedModel
import numpy as np

class AIMusicComposer:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = self.load_model()

    def load_model(self):
        config = configs.CONFIG_MAP['cat-mel_2bar_big']
        model = TrainedModel(config, batch_size=4, checkpoint_dir_or_path=self.model_path)
        return model

    def generate_music(self, num_steps=128, temperature=0.5):
        z = np.random.normal(size=(self.model.batch_size, self.model.z_size))
        generated_sequences = self.model.decode(z=z, length=num_steps, temperature=temperature)
        return generated_sequences

    def save_midi(self, sequence, output_dir='output'):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        midi_filename = os.path.join(output_dir, 'generated_music.mid')
        mm.sequence_proto_to_midi_file(sequence, midi_filename)
        print(f"Generated music saved to: {midi_filename}")

if __name__ == "__main__":
    model_path = '' #Sorry i didn't add path here for security
    composer = AIMusicComposer(model_path)
    generated_sequence = composer.generate_music()
    composer.save_midi(generated_sequence)
