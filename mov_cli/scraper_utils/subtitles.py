iso_639 = {"abkhazian": "ab", "afar": "aa", "afrikaans": "af", "akan": "ak", "albanian": "sq", "amharic": "am", "arabic": "ar", "aragonese": "an", "armenian": "hy", "assamese": "as", "avaric": "av", "avestan": "ae", "aymara": "ay", "azerbaijani": "az", "bambara": "bm", "bashkir": "ba", "basque": "eu", "belarusian": "be", "bengali": "bn", "bislama": "bi", "bosnian": "bs", "breton": "br", "bulgarian": "bg", "burmese": "my", "catalan": "ca", "chamorro": "ch", "chechen": "ce", "chichewa": "ny", "chinese": "zh", "church\u00a0slavonic": "cu", "chuvash": "cv", "cornish": "kw", "corsican": "co", "cree": "cr", "croatian": "hr", "czech": "cs", "danish": "da", "divehi": "dv", "dutch": "nl", "dzongkha": "dz", "english": "en", "esperanto": "eo", "estonian": "et", "ewe": "ee", "faroese": "fo", "fijian": "fj", "finnish": "fi", "french": "fr", "western frisian": "fy", "fulah": "ff", "gaelic": "gd", "galician": "gl", "ganda": "lg", "georgian": "ka", "german": "de", "greek": "el", "kalaallisut": "kl", "guarani": "gn", "gujarati": "gu", "haitian": "ht", "hausa": "ha", "hebrew": "he", "herero": "hz", "hindi": "hi", "hiri motu": "ho", "hungarian": "hu", "icelandic": "is", "ido": "io", "igbo": "ig", "indonesian": "id", "interlingua": "ia", "interlingue": "ie", "inuktitut": "iu", "inupiaq": "ik", "irish": "ga", "italian": "it", "japanese": "ja", "javanese": "jv", "kannada": "kn", "kanuri": "kr", "kashmiri": "ks", "kazakh": "kk", "central khmer": "km", "kikuyu": "ki", "kinyarwanda": "rw", "kirghiz": "ky", "komi": "kv", "kongo": "kg", "korean": "ko", "kuanyama": "kj", "kurdish": "ku", "lao": "lo", "latin": "la", "latvian": "lv", "limburgan": "li", "lingala": "ln", "lithuanian": "lt", "luba-katanga": "lu", "luxembourgish": "lb", "macedonian": "mk", "malagasy": "mg", "malay": "ms", "malayalam": "ml", "maltese": "mt", "manx": "gv", "maori": "mi", "marathi": "mr", "marshallese": "mh", "mongolian": "mn", "nauru": "na", "navajo": "nv", "north ndebele": "nd", "south ndebele": "nr", "ndonga": "ng", "nepali": "ne", "norwegian": "no", "norwegian bokm\u00e5l": "nb", "norwegian nynorsk": "nn", "sichuan yi": "ii", "occitan": "oc", "ojibwa": "oj", "oriya": "or", "oromo": "om", "ossetian": "os", "pali": "pi", "pashto": "ps", "persian": "fa", "polish": "pl", "portuguese": "pt", "punjabi": "pa", "quechua": "qu", "romanian": "ro", "romansh": "rm", "rundi": "rn", "russian": "ru", "northern sami": "se", "samoan": "sm", "sango": "sg", "sanskrit": "sa", "sardinian": "sc", "serbian": "sr", "shona": "sn", "sindhi": "sd", "sinhala": "si", "slovak": "sk", "slovenian": "sl", "somali": "so", "southern sotho": "st", "spanish": "es", "sundanese": "su", "swahili": "sw", "swati": "ss", "swedish": "sv", "tagalog": "tl", "tahitian": "ty", "tajik": "tg", "tamil": "ta", "tatar": "tt", "telugu": "te", "thai": "th", "tibetan": "bo", "tigrinya": "ti", "tonga": "to", "tsonga": "ts", "tswana": "tn", "turkish": "tr", "turkmen": "tk", "twi": "tw", "uighur": "ug", "ukrainian": "uk", "urdu": "ur", "uzbek": "uz", "venda": "ve", "vietnamese": "vi", "volap\u00fck": "vo", "walloon": "wa", "welsh": "cy", "wolof": "wo", "xhosa": "xh", "yiddish": "yi", "yoruba": "yo", "zhuang": "za", "zulu": "zu"}

def get_prefix(language) -> str:
    prefix = iso_639.get(language.lower(), None)
    return prefix

def get_language(prefix):
    key_list = list(iso_639.keys())
    val_list = list(iso_639.values())

    position = val_list.index(prefix)
    print(key_list[position])
