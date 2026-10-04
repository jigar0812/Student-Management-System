import os,tempfile,unittest
import database.database as db
import services.student_service as s
class Tests(unittest.TestCase):
 def setUp(self):
  self.f=tempfile.NamedTemporaryFile(delete=False); self.f.close(); self.old=db.DATABASE_PATH; db.DATABASE_PATH=self.f.name; db.initialize_database()
 def tearDown(self):
  db.DATABASE_PATH=self.old; os.remove(self.f.name)
 def data(self): return {'name':'Jigar Yadav','roll_no':'24119','email':'jigar@example.com','course':'Computer Engineering'}
 def test_validation(self): self.assertIsNone(s.validate_student(self.data()))
 def test_invalid_email(self): d=self.data(); d['email']='bad'; self.assertIsNotNone(s.validate_student(d))
 def test_crud(self):
  i=s.add_student(self.data()); self.assertEqual(s.get_student(i)['roll_no'],'24119'); d=self.data(); d['name']='Updated'; self.assertTrue(s.update_student(i,d)); self.assertEqual(s.get_student(i)['name'],'Updated'); self.assertTrue(s.delete_student(i)); self.assertIsNone(s.get_student(i))
 def test_search(self): s.add_student(self.data()); self.assertEqual(len(s.search_students('Jigar')),1)
if __name__=='__main__': unittest.main()
