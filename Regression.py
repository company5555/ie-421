import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Veri setini oluştur
data = {
    "Agriculture, forestry, fishing, and hunting": {"2023": 55689, "2024": 53359, "2025": 54579, "2026": 55799, "2027": 57019, "2028": 58239, "2029": 59458, "2030": 60678, "2031": 61898, "2032": 63118, "2033": 64338},
    "Mining": {"2023": 72886, "2024": 82052, "2025": 83988, "2026": 85925, "2027": 87861, "2028": 89798, "2029": 91734, "2030": 93671, "2031": 95607, "2032": 97544, "2033": 99480},
    "Utilities": {"2023": 75770, "2024": 71410, "2025": 72884, "2026": 74358, "2027": 75832, "2028": 77306, "2029": 78781, "2030": 80255, "2031": 81729, "2032": 83203, "2033": 84677},
    "Construction": {"2023": 634697, "2024": 544486, "2025": 557612, "2026": 570737, "2027": 583863, "2028": 596989, "2029": 610114, "2030": 623240, "2031": 636366, "2032": 649491, "2033": 662617},
    "Manufacturing": {"2023": 1083951, "2024": 955455, "2025": 968174, "2026": 980894, "2027": 993613, "2028": 1006332, "2029": 1019052, "2030": 1031771, "2031": 1044491, "2032": 1057210, "2033": 1069930},
    "Retail trade": {"2023": 659293, "2024": 612271, "2025": 624474, "2026": 636677, "2027": 648880, "2028": 661082, "2029": 673285, "2030": 685488, "2031": 697691, "2032": 709893, "2033": 722096},
    "Transportation and warehousing": {"2023": 448489, "2024": 376611, "2025": 386722, "2026": 396833, "2027": 406945, "2028": 417056, "2029": 427167, "2030": 437279, "2031": 447390, "2032": 457501, "2033": 467613},
    "Information": {"2023": 465671, "2024": 395393, "2025": 405420, "2026": 415448, "2027": 425475, "2028": 435502, "2029": 445529, "2030": 455556, "2031": 465583, "2032": 475610, "2033": 485637},
    "Finance and insurance": {"2023": 911932, "2024": 852483, "2025": 874607, "2026": 896730, "2027": 918853, "2028": 940976, "2029": 963099, "2030": 985223, "2031": 1007346, "2032": 1029469, "2033": 1051592},
    "Real estate and rental and leasing": {"2023": 187898, "2024": 166855, "2025": 171309, "2026": 175762, "2027": 180215, "2028": 184669, "2029": 189122, "2030": 193575, "2031": 198029, "2032": 202482, "2033": 206935},
    "Management of companies and enterprises": {"2023": 379764, "2024": 359203, "2025": 369895, "2026": 380587, "2027": 391279, "2028": 401971, "2029": 412663, "2030": 423355, "2031": 434047, "2032": 444739, "2033": 455431},
    "Educational services": {"2023": 206505, "2024": 200831, "2025": 206628, "2026": 212425, "2027": 218221, "2028": 224018, "2029": 229815, "2030": 235611, "2031": 241408, "2032": 247204, "2033": 253001},
    "Health care and social assistance": {"2023": 1377762, "2024": 1271409, "2025": 1308362, "2026": 1345315, "2027": 1382269, "2028": 1419222, "2029": 1456175, "2030": 1493128, "2031": 1530081, "2032": 1567034, "2033": 1603988},
    "Arts, entertainment, and recreation": {"2023": 135172, "2024": 117927, "2025": 121023, "2026": 124118, "2027": 127214, "2028": 130310, "2029": 133406, "2030": 136501, "2031": 139597, "2032": 142693, "2033": 145789},
    "Accommodation and food services": {"2023": 477843, "2024": 409186, "2025": 420773, "2026": 432359, "2027": 443945, "2028": 455531, "2029": 467117, "2030": 478703, "2031": 490289, "2032": 501875, "2033": 513461},
    "Government": {"2023": 1732777, "2024": 1652224, "2025": 1687945, "2026": 1723667, "2027": 1759389, "2028": 1795110, "2029": 1830832, "2030": 1866553, "2031": 1902275, "2032": 1937997, "2033": 1973718}
}

# DataFrame'e çevir
df = pd.DataFrame(data).transpose()

def plot_sectors(selected_sectors=None):
    if selected_sectors is None:
        selected_sectors = ['Health care and social assistance', 'Government', 'Manufacturing']
    
    plt.figure(figsize=(15, 8))
    
    # Her seçili sektör için çizgi grafiği oluştur
    for sector in selected_sectors:
        plt.plot(df.columns, df.loc[sector], marker='o', label=sector, linewidth=2)
    
    # Grafik özelliklerini ayarla
    plt.title('Sektör Tahminleri 2023-2033', fontsize=14, pad=20)
    plt.xlabel('Yıl', fontsize=12)
    plt.ylabel('Birim (Bin)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Y ekseni değerlerini bin cinsinden göster
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x/1000):,}K'))
    
    # X ekseni etiketlerini döndür
    plt.xticks(rotation=45)
    
    # Grafik düzenini ayarla
    plt.tight_layout()
    
    return plt

# Örnek kullanım:
def main():
    # Tüm sektörleri göster
    print("Mevcut sektörler:")
    for i, sector in enumerate(df.index, 1):
        print(f"{i}. {sector}")
    
    # Kullanıcıdan sektör seçimini al
    print("\nGörmek istediğiniz sektörlerin numaralarını virgülle ayırarak girin (örn: 1,2,3):")
    selections = input()
    
    try:
        # Seçilen sektörleri al
        selected_indices = [int(x.strip()) - 1 for x in selections.split(',')]
        selected_sectors = [df.index[i] for i in selected_indices]
        
        # Grafiği çiz
        plot_sectors(selected_sectors)
        plt.show()
        
    except Exception as e:
        print("Hata oluştu. Lütfen geçerli sektör numaraları girin.")
        print(f"Hata detayı: {e}")

if __name__ == "__main__":
    main()