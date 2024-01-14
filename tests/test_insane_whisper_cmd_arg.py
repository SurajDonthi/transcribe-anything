"""
Tests transcribe_anything
"""

# pylint: disable=bad-option-value,useless-option-value,no-self-use,protected-access,R0801
# flake8: noqa E501

import os
import unittest
import shutil

from transcribe_anything.api import transcribe

from transcribe_anything.insanely_fast_whisper import has_nvidia_smi


HERE = os.path.abspath(os.path.dirname(__file__))
LOCALFILE_DIR = os.path.join(HERE, "localfile")
TESTS_DATA_DIR = os.path.join(LOCALFILE_DIR, "text_video_api_insane", "en")


class InsaneWhisperModeTester(unittest.TestCase):
    """Tester for transcribe anything."""

    @unittest.skipUnless(has_nvidia_smi(), "No GPU detected")
    def test_local_file(self) -> None:
        """Check that the command works on a local file."""
        shutil.rmtree(TESTS_DATA_DIR, ignore_errors=True)
        vidfile = os.path.join(LOCALFILE_DIR, "video.mp4")
        transcribe(
            url_or_file=vidfile,
            language="en",
            model="tiny",
            device="insane",
            output_dir=TESTS_DATA_DIR,
        )
        # check that theres a vtt file
        vtt_file = os.path.join(TESTS_DATA_DIR, "out.vtt")
        self.assertTrue(os.path.isfile(vtt_file))
        print(f"Found expected vtt file: {vtt_file}")
        # srt file
        srt_file = os.path.join(TESTS_DATA_DIR, "out.srt")
        self.assertTrue(os.path.isfile(srt_file))
        print(f"Found expected srt file: {srt_file}")


if __name__ == "__main__":
    unittest.main()
