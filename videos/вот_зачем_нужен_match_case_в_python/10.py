from dataclasses import dataclass

@dataclass
class Config:
    debug: bool
    port: int = 4444

def get_current_config(instance: Config):
    match instance:
        case Config(debug=False):
            print(f"The program is running: {instance.port}")
        case Config(debug=True):
            print("The program is running in debugging mode")
        case Config(_, _):
            print("¯\_()_/¯")

get_current_config(Config(debug=False, port=8080))
