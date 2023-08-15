#ApplyForJob
class ApplyForJob:
  def __init__(self, position, company, applicant_name, email, resume):
    self.postion = position
    self.company = company
    self.applicant_name = applicant_name
    self.email = email
    self.resume = resume
    self.status = "Pending"
    self.interview_data = None

  def Submit_application(self):
    if self.resume and self.applicant_name and self.email:
      self.status = "Completed"
      return True
    else:
      return False

  def schedule_interview(self, date):
    if self.status == "Completed":
      self.status = "Schedule"
      self.date = date
      return True
    else:
      return False


  def update_status(self, status):
    self.status = status

  def get_status(self):
    return self.status

applicant1 = ApplyForJob("DataScientest", "Apple", "Ankon", "ankonDataScientest@gmail.com", "Resume.pdf")

if applicant1.Submit_application():
  print("Application is Submited Succesfully")

else:
  print("Application Submision Failed please provide everything")

if applicant1.schedule_interview("2023-09-01"):
    print("Interview scheduled successfully.")
else:
    print("Interview scheduling failed. Application must be submitted first.")


applicant1.update_status("OFFER Accepted")

print(f"Application status is: {applicant1.get_status()} \nYour name is: {applicant1.applicant_name}")