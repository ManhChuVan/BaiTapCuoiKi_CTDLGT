class TuDien:
  def __init__(self):
      self.dic = {}

  def bam(self, tu):
      return tu[0].lower()

  def NhapTu(self, tu, dongnghia=None, trai_nghia=None):
      key = self.bam(tu)
      if key in self.dic:
          self.dic[key][tu] = {"DongNghia": dongnghia, "TraiNghia": trai_nghia}
      else:
          self.dic[key] = {tu: {"DongNghia": dongnghia, "TraiNghia": trai_nghia}}

  def DongNghia(self, tu):
      key = self.bam(tu)
      if key in self.dic and tu in self.dic[key]:
          return self.dic[key][tu]["DongNghia"]
      return None

  def TraiNghia(self, tu):
      key = self.bam(tu)
      if key in self.dic and tu in self.dic[key]:
          return self.dic[key][tu]["TraiNghia"]
      return None

# Test
tudien = TuDien()
tudien.NhapTu("apple", ["quả táo", "trái táo"], ["quả mận", "trái mận"])
tudien.NhapTu("banana", ["quả chuối"], ["quả táo", "quả mận"])
tudien.NhapTu("ball", ["quả bóng"], ["quả bóng rổ"])
# tudien.NhapTu("ball", ["quả banh"], ["quả bóng rổ"])


print("Đồng nghĩa của từ 'apple':", tudien.DongNghia("apple"))
print("Trái nghĩa của từ 'apple':", tudien.TraiNghia("apple"))

print("Đồng nghĩa của từ 'banana':", tudien.DongNghia("banana"))
print("Trái nghĩa của từ 'banana':", tudien.TraiNghia("banana")) 

print("Đồng nghĩa của từ 'ball':", tudien.DongNghia("ball")) 
print("Trái nghĩa của từ 'ball':", tudien.TraiNghia("ball")) 

print(tudien.dic)
