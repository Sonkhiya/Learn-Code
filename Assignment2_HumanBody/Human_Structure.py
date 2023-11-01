from abc import ABC, abstractmethod

class EyeComponent(ABC):
    @abstractmethod
    def process_light(self, light_intensity):
        pass

class Cornea(EyeComponent):
    def process_light(self, light_intensity):
        if light_intensity > 7:
            print("Light is bent as it passes through the cornea.")
        else:
            print("No light. Unable to see.")

class Pupil(EyeComponent):
    def process_light(self, light_intensity):
        if light_intensity > 7:
            print("The iris adjusts the pupil to control the amount of light entering the eye.")
        else:
            print("No light. Unable to see.")

class Lens(EyeComponent):
    def process_light(self, light_intensity):
        if light_intensity > 7:
            print("The lens and cornea work together to focus light on the retina.")
        else:
            print("No light. Unable to see.")

class Retina(EyeComponent):
    def process_light(self, light_intensity):
        if light_intensity > 7:
            print("Photoreceptors in the retina convert light into electrical signals.")
        else:
            print("No light. Unable to see.")

class OpticNerve(EyeComponent):
    def process_light(self, light_intensity):
        if light_intensity > 7:
            print("Electrical signals travel through the optic nerve to the brain.")
        else:
            print("No light. Unable to see.")

class Tear(EyeComponent):
    def process_light(self, light_intensity):
        if light_intensity > 7:
            print("Tears keep the eye moist and clean for proper functioning.")
        else:
            print("No light. Unable to see.")

class Eye:
    def __init__(self):
        self.components = [
            Cornea(),
            Pupil(),
            Lens(),
            Retina(),
            OpticNerve(),
            Tear()
        ]

    def process_light_through_eye(self, light_intensity):
        for component in self.components:
            component.process_light(light_intensity)



light_intensity = 5  
human_eye = Eye()
human_eye.process_light_through_eye(light_intensity)

if light_intensity > 5:
    print("You can see the tree!")
else:
    print("Unable to see the tree.")
