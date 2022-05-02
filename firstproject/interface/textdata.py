import spacy

spacy.prefer_gpu()
nlp = spacy.load("pt_core_news_lg")
all_stop_words = nlp.Defaults.stop_words


class TextManipulation:

    def printamermo(self):
        print("aaaaaaa")

    # Caso for salvar os arquivos e ler eles, basta passar o path deles para essa função
    def read_text(self, text):
        text = open(text, mode="r", encoding="utf-8").read()
        return text

    def segmentation_based_sentences(self, text):
        originaltext_segmented = []
        doc = nlp(text)

        for sentence in doc.sents:
            sentence_source = self.remove_only_spaces(sentence)
            sentence_clean = self.remove_stop_words_puncts_spaces(sentence)
            if len(sentence_clean) > 0:
                originaltext_segmented.append((sentence_source, sentence_clean))

        return originaltext_segmented

    def remove_stop_words_puncts_spaces(self, sentence):
        sentence_result = []
        for token in sentence:
            if token.tag_ != "SPACE" and token.tag_ != "PUNCT" and token.text not in all_stop_words \
                    and token.lemma_ not in all_stop_words:
                sentence_result.append(token)
        return sentence_result

    def remove_only_spaces(self, sentence):
        sentence_result = []
        for token in sentence:
            if token.tag_ != "SPACE":
                sentence_result.append(token)
        return sentence_result
