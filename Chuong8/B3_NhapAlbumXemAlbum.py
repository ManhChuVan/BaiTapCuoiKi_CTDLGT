class BaiHat:
  def __init__(self, ten_bai_hat, ten_nhac_si, ten_ca_si):
      self.ten_bai_hat = ten_bai_hat
      self.ten_nhac_si = ten_nhac_si
      self.ten_ca_si = ten_ca_si

class Album:
  def __init__(self, ten_album):
      self.ten_album = ten_album
      self.bai_hats = []

  def them_bai_hat(self, bai_hat):
      self.bai_hats.append(bai_hat)

class TuDien:
  def __init__(self):
      self.dic = {}

  def bam(self, ten_album):
      return ten_album.lower()

  def NhapAlbum(self, ten_album, danh_sach_bai_hat):
      key = self.bam(ten_album)
      if key not in self.dic:
          self.dic[key] = Album(ten_album)
      album = self.dic[key]
      for bai_hat in danh_sach_bai_hat:
          album.them_bai_hat(bai_hat)

  def XemAlbum(self, ten_album):
      key = self.bam(ten_album)
      if key in self.dic:
          album = self.dic[key]
          print("Thông tin album '{}'".format(album.ten_album))
          for i, bai_hat in enumerate(album.bai_hats, 1):
              print("{}. Tên bài hát: {}, Nhạc sĩ: {}, Ca sĩ: {}".format(i, bai_hat.ten_bai_hat, bai_hat.ten_nhac_si, bai_hat.ten_ca_si))
      else:
          print("Album '{}' không tồn tại trong từ điển.".format(ten_album))

# Test
tudien = TuDien()

danh_sach_bai_hat_1 = [
  BaiHat("Em gái mưa", "Mr. Siro", "Hương Tràm"),
  BaiHat("Chẳng thể giữ lấy", "Phạm Thanh Hà", "Hương Ly")
]
danh_sach_bai_hat_2 = [
  BaiHat("Gặp nhưng không ở lại", "Đức Phúc", "Đức Phúc"),
  BaiHat("Sau tất cả", "Erik", "Erik"),
  BaiHat("Cô gái ngày hôm qua", "Đức Phúc", "Đức Phúc")
]

tudien.NhapAlbum("Những bài hát hay nhất của Hương Tràm", danh_sach_bai_hat_1)
tudien.NhapAlbum("Những ca khúc đình đám của Đức Phúc", danh_sach_bai_hat_2)

tudien.XemAlbum("Những bài hát hay nhất của Hương Tràm")
tudien.XemAlbum("Những ca khúc đình đám của Đức Phúc")
tudien.XemAlbum("Album không tồn tại")
