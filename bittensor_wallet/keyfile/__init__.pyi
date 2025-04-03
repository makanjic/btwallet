from typing import Optional

from ..keypair import Keypair


class Keyfile:
    def __init__(
            self,
            path: Optional[str] = None,
            name: Optional[str] = None,
            should_save_to_env: bool = False,
    ) -> None: ...

    def __str__(self) -> str: ...

    @property
    def path(self) -> str: ...

    def exists_on_device(self) -> bool: ...

    def is_readable(self) -> bool: ...

    def is_writable(self) -> bool: ...

    def is_encrypted(self) -> bool: ...

    def check_and_update_encryption(
            self, print_result: bool = True, no_prompt: bool = False
    ) -> None: ...

    def encrypt(self, password: Optional[str] = None) -> None: ...

    def decrypt(self, password: Optional[str] = None) -> None: ...

    def env_var_name(self) -> str: ...

    def save_password_to_env(self, password: Optional[str] = None) -> None: ...

    def remove_password_from_env(self) -> None: ...

    @property
    def keypair(self) -> "Keypair": ...

    def get_keypair(self, password: Optional[str] = None) -> "Keypair": ...

    def set_keypair(
            self,
            keypair: "Keypair",
            encrypt: bool = True,
            overwrite: bool = False,
            password: Optional[str] = None,
    ) -> None: ...

    @property
    def data(self): ...

    def make_dirs(self): ...


def serialized_keypair_to_keyfile_data(keypair: "Keypair") -> bytes: ...


def deserialize_keypair_from_keyfile_data(keyfile_data: bytes) -> "Keypair": ...


def validate_password(password: str) -> bool: ...


def ask_password(validation_required: bool) -> str: ...


def legacy_encrypt_keyfile_data(
        keyfile_data: bytes, password: Optional[str] = None
) -> bytes: ...


def get_password_from_environment(env_var_name: str) -> Optional[str]: ...


def encrypt_keyfile_data(
        keyfile_data: bytes, password: Optional[str] = None
) -> bytes: ...


def decrypt_keyfile_data(
        keyfile_data: bytes,
        password: Optional[str] = None,
        password_env_var: Optional[str] = None,
) -> bytes: ...


def keyfile_data_is_encrypted_nacl(keyfile_data: bytes) -> bool: ...


def keyfile_data_is_encrypted_ansible(keyfile_data: bytes) -> bool: ...


def keyfile_data_is_encrypted_legacy(keyfile_data: bytes) -> bool: ...


def keyfile_data_is_encrypted(keyfile_data: bytes) -> bool: ...


def keyfile_data_encryption_method(keyfile_data: bytes) -> str: ...