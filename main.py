meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "Tanggapan terhadap lelucon",
            "SHEESH": "Sedikit ketidaksetujuan",
            "CREEPY": "Menakutkan, tidak menyenangkan",
            "AGGRO": "Untuk menjadi agresif/marah",
            "FR": "Singkatan dari 'For Real' untuk menyatakan fakta",
            "NGL": "Singkatan dari 'Not Gonna Lie' untuk menyatakan tidak berbohong"
}

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print("Makna kata", word, "adalah",meme_dict[word])
else:
    print("Kata tersebut tidak ada")
