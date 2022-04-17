import pathlib
from contextlib import suppress

import pytest
from vivaldi_feed_exporter.main import parse_args


class TestParseArgs:
    def test_profile_folder_mandatory(self):
        """profile-folderは必須"""
        with pytest.raises(BaseException), suppress(NotImplementedError):
            parse_args(())

    def test_profile_folder_exists(self, tmp_path: pathlib.Path):
        """profile-folderは存在する"""
        with pytest.raises(BaseException), suppress(NotImplementedError):
            parse_args((str(tmp_path / "nonexistent"),))

    def test_profile_folder_directory(self, tmp_path: pathlib.Path):
        """profile-folderはディレクトリ"""
        filepath = tmp_path / "empty"
        with open(filepath, "wb") as _:
            pass
        with pytest.raises(BaseException), suppress(NotImplementedError):
            parse_args((str(filepath),))

    def test_profile_folder(self, tmp_path: pathlib.Path):
        assert parse_args((str(tmp_path),)).profile_folder == tmp_path
