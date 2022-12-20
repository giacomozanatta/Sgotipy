from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SgotipyStatusRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SgotipyStatusResponse(_message.Message):
    __slots__ = ["current_song", "device", "device_status", "status"]
    CURRENT_SONG_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    current_song: Song
    device: str
    device_status: str
    status: str
    def __init__(self, status: _Optional[str] = ..., device: _Optional[str] = ..., device_status: _Optional[str] = ..., current_song: _Optional[_Union[Song, _Mapping]] = ...) -> None: ...

class Song(_message.Message):
    __slots__ = ["artists", "id", "title"]
    ARTISTS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    artists: str
    id: str
    title: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., artists: _Optional[str] = ...) -> None: ...

class StartSgotipyRequest(_message.Message):
    __slots__ = ["access_token", "expires_in", "refresh_token", "scope", "token_type"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    expires_in: int
    refresh_token: str
    scope: str
    token_type: str
    def __init__(self, access_token: _Optional[str] = ..., token_type: _Optional[str] = ..., scope: _Optional[str] = ..., expires_in: _Optional[int] = ..., refresh_token: _Optional[str] = ...) -> None: ...

class StartSgotipyResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class StopSgotipyRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StopSgotipyResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
