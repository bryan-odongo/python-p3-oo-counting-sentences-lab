#!/usr/bin/env python3
import re


class MyString:
    def __init__(self, string=""):
        self.string = string

    @property
    def value(self):
        return self._string

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._string = value

        else:
            print("The value must be a string.")

    def is_sentence(self):
        return True if self.string.endswith(".") else False

    def is_question(self):
        return True if self.string.endswith("?") else False

    def is_exclamation(self):
        return True if self.string.endswith("!") else False

    def count_sentences(self):
        sentences = re.split(r"[.!?]", self.string)

        sentences = [string for string in sentences if string.strip()]
        return len(sentences)
