from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `neosantara.resources` module.

    This is used so that we can lazily import `neosantara.resources` only when
    needed *and* so that users can just import `neosantara` and reference `neosantara.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("neosantara.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
