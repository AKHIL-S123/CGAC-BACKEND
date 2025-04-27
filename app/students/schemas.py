from pydantic import BaseModel,Field
from typing import Optional

class StudentSchema(BaseModel):
    batch:Optional[str]
    applicationNumber: Optional[str]
    rank: Optional[str]
    registerNo: Optional[str]
    rollNo: Optional[str]
    emisNo: Optional[str]
    umisNo: Optional[str]
    degree: Optional[str]
    course: Optional[str]
    mediumOfStudy: Optional[str]
    percentageOfMarks: Optional[str]
    name: Optional[str]
    mobile: Optional[str]
    whatsappNo: Optional[str]
    email: Optional[str]
    aadhaarNumber: Optional[str]
    religion: Optional[str]
    community: Optional[str]
    caste: Optional[str]
    communityCertificateNo: Optional[str]
    dateOfBirth: Optional[str]
    gender: Optional[str]
    bloodGroup: Optional[str]
    pwd: Optional[str]
    typesOfDisability: Optional[str]
    percentageOfDisability: Optional[str]
    exServiceMan: Optional[str]
    ncc: Optional[str]
    sports: Optional[str]
    categoryOfSports: Optional[str]
    admissionQuota: Optional[str]
    dateOfAdmission: Optional[str]
    admissionNumber: Optional[str]
    presentAddress: Optional[str]
    communicationAddress: Optional[str]
    fatherName: Optional[str]
    fatherMobile: Optional[str]
    fathersOccupation: Optional[str]
    fathersEducation: Optional[str]
    motherName: Optional[str]
    motherMobile: Optional[str]
    mothersOccupation: Optional[str]
    mothersEducation: Optional[str]
    guardianName: Optional[str]
    guardianNumber: Optional[str]
    singleParent: Optional[str]
    firstGraduate: Optional[str]
    firstGraduateCertificateNo: Optional[str]
    incomeCertificateNo: Optional[str]
    annualIncome: Optional[str]

    viStandardSchoolName: Optional[str]
    viStandardCity: Optional[str]
    viStandardType: Optional[str]
    viStandardYearStart: Optional[str]
    viStandardYearEnd: Optional[str]

    viiStandardSchoolName: Optional[str]
    viiStandardCity: Optional[str]
    viiStandardType: Optional[str]
    viiStandardYearStart: Optional[str]
    viiStandardYearEnd: Optional[str]

    viiiStandardSchoolName: Optional[str]
    viiiStandardCity: Optional[str]
    viiiStandardType: Optional[str]
    viiiStandardYearStart: Optional[str]
    viiiStandardYearEnd: Optional[str]

    ixStandardSchoolName: Optional[str]
    ixStandardCity: Optional[str]
    ixStandardType: Optional[str]
    ixStandardYearStart: Optional[str]
    ixStandardYearEnd: Optional[str]

    xStandardSchoolName: Optional[str]
    xStandardCity: Optional[str]
    xStandardType: Optional[str]
    xStandardYearStart: Optional[str]
    xStandardYearEnd: Optional[str]

    xiStandardSchoolName: Optional[str]
    xiStandardCity: Optional[str]
    xiStandardType: Optional[str]
    xiStandardYearStart: Optional[str]
    xiStandardYearEnd: Optional[str]

    xiiStandardSchoolName: Optional[str]
    xiiStandardCity: Optional[str]
    xiiStandardType: Optional[str]
    xiiStandardYearStart: Optional[str]
    xiiStandardYearEnd: Optional[str]

    bankName: Optional[str]
    branch: Optional[str]
    ifsc: Optional[str]
    micr: Optional[str]
    accountType: Optional[str]
    bankAccountNo: Optional[str]
    hostlerOrDayScholar: Optional[str]

class UpdateStudentSchema(StudentSchema):
    pass


class StudentListQuery(BaseModel):
    page: int = Field(default=1, ge=1, description="Page number, must be 1 or greater")
    sort_by:Optional[str] = Field(default='')
    sort_dir: Optional[str] = Field(default='')
    limit: int = Field(default=10, ge=1, le=100, description="Number of items per page (max 100)")
    search: Optional[str] = Field(default='', description="Search keyword for filtering students")
    community: Optional[str] = Field(default='', description="Community identifier for filtering students")
    batch:int=0


