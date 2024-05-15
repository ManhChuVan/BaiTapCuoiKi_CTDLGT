class TuDien:
  def __init__(self):
      self.dic = {}

  def bam(self, tu):
      return tu[0].lower()

  def NhapTu(self, tu, dongnghia=None, trai_nghia=None):
      key = self.bam(tu)
      if key in self.dic:
          self.dic[key].append((tu, dongnghia, trai_nghia))
      else:
          self.dic[key] = [(tu, dongnghia, trai_nghia)]

  def TraTu(self, tu):
      key = self.bam(tu)
      if key in self.dic:
          for entry in self.dic[key]:
              if entry[0] == tu:
                  return entry[1], entry[2]
      return None, None

# Test
tudien = TuDien()
tudien.NhapTu("apple", "quả táo", "không có")
tudien.NhapTu("banana", "quả chuối", "không có")
tudien.NhapTu("ball", "quả bóng", "không có")

dong_nghia, trai_nghia = tudien.TraTu("banana")
print("Đồng nghĩa của từ 'banana':", dong_nghia)  
print("Trái nghĩa của từ 'banana':", trai_nghia) 

dong_nghia, trai_ngghia = tudien.TraTu("ball")
print("Đồng nghĩa của từ 'ball':", dong_nghia) 
print("Trái nghĩa của từ 'ball':", trai_nghia)


print(tudien.dic)