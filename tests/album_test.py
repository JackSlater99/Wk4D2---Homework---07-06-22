import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):
    
    def setUp(self):
        self.album = Album("Piano Man", "Pop Rock", "Billy Joel")
    
    
    def test_album_has_title(self):
        self.assertEqual("Piano Man", self.album.title)
        
        
    def test_album_has_genre(self):
        self.assertEqual("Pop Rock", self.album.genre)
       
        
    def test_album_has_artist(self):
        self.assertEqual("Billy Joel", self.album.artist)
    
    
    
    
   