from wordcloud import WordCloud
import matplotlib.pyplot as plt
import string

def generate_wordcloud(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        text = text.lower()

        for p in string.punctuation:
            text = text.replace(p, " ")

        wc = WordCloud(
            width=800,
            height=400,
            background_color="white"
        ).generate(text)

        wc.to_file("wordcloud.png")
        print("Word cloud berhasil dibuat: wordcloud.png")

        plt.figure(figsize=(10, 5))
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        plt.show()

    except FileNotFoundError:
        print("Error: file tidak ditemukan.")


if __name__ == "__main__":
    filename = input("Masukkan nama file teks: ")
    generate_wordcloud(filename)