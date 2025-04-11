from tinydb import TinyDB, Query
from pathlib import Path
from typing import cast

# przykład zastosowania wzorca projektowego Adapter

class DBTiny:
    def __init__(self, db_dir: Path, db_file_prefix: str) -> None:
        self._db = TinyDB(
        path=db_dir / f"{db_file_prefix}.json", create_dirs=True)

    def create(self, item: dict) -> int:
        return cast(int, self._db.insert(item))

    def get(self, idx: int | list[int]) -> dict:
        if isinstance(idx, int):
            return cast(dict, self._db.get(doc_ids=idx))
        return cast(self._db.get(doc_id=idx))

    def read_all(self) -> list[dict]:
        return cast(list[dict], self._db.all())

    def filter(self, **kwargs) -> list[dict]:
        query = Query()

        for k, v in kwargs.items():
            query &= query[k] == v

        return cast(list[dict], self._db.search(query))

    def count(self) -> int:
        return len(self._db)

    def create_many(self, items: list[dict]) -> list[int]:
        return cast(list[int], self._db.insert_multiple(items))

    def __enter__(self) -> "DBTiny":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._db.close()
