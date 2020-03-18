# SPDX-FileCopyrightText: 2020 Hlib Babii <hlibbabii@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0

import os
import shutil

import codeprep.api.corpus as api
from codeprep.config import root_package_dir

PATH_TO_TEST_CORPUS = os.path.join(root_package_dir, '..', 'test-data', 'test-corpus')
TEST_OUTPUT = os.path.join(root_package_dir, '..', 'test-output')


def test_preprocess_with_different_options():
    calc_vocab = False
    api.basic(path=PATH_TO_TEST_CORPUS, extensions="java", output_path=TEST_OUTPUT)
    api.basic(path=PATH_TO_TEST_CORPUS, extensions="java", split_numbers=True, ronin=True, stem=True,
              no_spaces=True, no_unicode=True, no_case=True, no_com=True, no_str=True, max_str_length=30,
              calc_vocab=calc_vocab, output_path=TEST_OUTPUT)
    api.chars(path=PATH_TO_TEST_CORPUS, extensions="java", output_path=TEST_OUTPUT)
    api.nosplit(path=PATH_TO_TEST_CORPUS, extensions="java", output_path=TEST_OUTPUT)
    api.bpe(path=PATH_TO_TEST_CORPUS, bpe_codes_id='10k', extensions="java", output_path=TEST_OUTPUT)


def teardown_function(function):
    print(f'Removing the outputs at: {TEST_OUTPUT}')
    shutil.rmtree(TEST_OUTPUT)
