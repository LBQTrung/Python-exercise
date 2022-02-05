# CHƯƠNG TRÌNH PYTHON CHUYỂN CÂU CÓ DẤU SANG DẠNG KHÔNG DẤU:
# vd: "một hai ba." --> "mot-hai-ba"

# Giá trị mục tiêu muốn chuyển thành: 
TARGET = {
    '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹêềếểễệ]': 'e',
    '[ìíỉĩị]': 'i',
    '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụưừứửữự]': 'u',
    '[ỳýỷỹỵ]': 'y'
}

'''
function convert_word(): chuyển Từ có dấu sang Từ không dấu.
input: từ có dấu
output: từ không dấu
'''
def convert_word(word):
    result = ''
    for letter in word:
        for key in TARGET.keys():
            if letter in key:
                result += TARGET[key]
                break
        else:
            result += letter
    return result

'''
function convert(): chuyển câu có dấu bình thường thành câu được yêu cầu
input: chuỗi chứa câu cần chuyển
output: kết quả chuỗi theo yêu cầu bài toán 
'''    
def convert(data):
    #Chuyển thành chữ thường, xóa dấu chấm
    lower_string = data.lower()
    lower_string = lower_string.strip(".")

    # word_list chứa từ của câu cần convert
    word_list = lower_string.split(" ")

    #Convert sang dạng không dấu và chuyển thành kết quả phù hợp
    result = [convert_word(word) for word in word_list]
    result = "-".join(result)
    return result

def main():
    print(convert("Việt Nam Quê Hương tôi."))

if __name__ == "__main__":
    main()