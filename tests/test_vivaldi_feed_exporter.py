import pathlib
from contextlib import suppress

import pytest
from vivaldi_feed_exporter import __version__, main


def test_version():
    assert __version__ == "0.1.0"


class TestParseArgs:
    def test_profile_folder_mandatory(self):
        """profile-folderは必須"""
        with pytest.raises(BaseException), suppress(NotImplementedError):
            main.parse_args(())

    def test_profile_folder_argument(self):
        """profile-folderは引数を取る"""
        with pytest.raises(BaseException), suppress(NotImplementedError):
            main.parse_args(("-p",))

    def test_profile_folder_exists(self, tmp_path: pathlib.Path):
        """profile-folderは存在する"""
        with pytest.raises(BaseException), suppress(NotImplementedError):
            main.parse_args(("-p", str(tmp_path / "nonexistent")))

    def test_profile_folder_directory(self, tmp_path: pathlib.Path):
        """profile-folderはディレクトリ"""
        filepath = tmp_path / "empty"
        with open(filepath, "w") as _:
            pass
        with pytest.raises(BaseException), suppress(NotImplementedError):
            main.parse_args(("-p", str(filepath)))

    def test_profile_folder(self, tmp_path: pathlib.Path):
        pathstr = str(tmp_path)
        assert main.parse_args(("-p", pathstr)).profile_folder == tmp_path
        assert main.parse_args(("--profile-folder", pathstr)).profile_folder == tmp_path
