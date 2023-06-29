from linkedin_api import Linkedin

# Authenticate using any Linkedin account credentials
api = Linkedin('nbscerbakov@gmail.com', '1l0v3fl0r1da')

jobs_qa_list = api.search_jobs(keywords='quality assurance',listed_at='86040000', limit=-1)
for i in range (0,len(jobs_qa_list)):   
    x,jobs_list_id = jobs_qa_list[i]["dashEntityUrn"].split("urn:li:fsd_jobPosting:")
    # print (jobs_list_id)

    job_details = api.get_job(jobs_list_id)
    # print (job_details,"\n")
        
    try:
        complex_Onsite_Apply = job_details["applyMethod"]['com.linkedin.voyager.jobs.ComplexOnsiteApply']
        print ("\n",jobs_list_id,"Company: ",job_details['companyDetails']['com.linkedin.voyager.deco.jobs.web.shared.WebCompactJobPostingCompany']['companyResolutionResult'] 
['name']," Role: ", job_details["title"])
        print ("\n",jobs_list_id, complex_Onsite_Apply,"\n")
        
    except Exception as e:
        print ("ERROR: ",e,jobs_list_id,"Company: ",job_details['companyDetails']['com.linkedin.voyager.deco.jobs.web.shared.WebCompactJobPostingCompany']['companyResolutionResult'] 
['name']," Role: ", job_details["title"])
