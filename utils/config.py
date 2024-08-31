import os
from typing import List, Any, get_type_hints
from dotenv import load_dotenv


def load_env_file(file_path: str):
    load_dotenv(file_path)


def config_properties(prefix: str):
    def decorator(cls):
        def init_config(self):
            hints = get_type_hints(cls)
            for key, hint in hints.items():
                env_key = f"{prefix.upper()}_{key.upper()}"
                value = os.getenv(env_key)
                if value is not None:
                    if hint == List[str]:
                        setattr(self, key, [item.strip() for item in value.split(',')])
                    elif hint == List[int]:
                        setattr(self, key, [int(item.strip()) for item in value.split(',')])
                    elif hint == int:
                        setattr(self, key, int(value))
                    elif hint == bool:
                        setattr(self, key, value.lower() in ('true', '1', 'yes'))
                    else:
                        setattr(self, key, value)

        cls.__init__ = init_config
        return cls

    return decorator


@config_properties(prefix="auth.security")
class SecurityPropertiesConfig:
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    REGION: str
    PASSWORD: str
    USER: str
    HOST: str
    DATABASE: str
    SF_USER: str
    SF_PASSWORD: str
    SF_ACCOUNT: str


# Usage
load_env_file(r'/Users/lalitmoharana/Documents/codes/personal/cortex-rag/.env')  # Load the .env file
config = SecurityPropertiesConfig()