

![](https://komarev.com/ghpvc/?username=jesvi)


##################### ER table
 
CREATE TABLE Student
(
    StudentId INTEGER,
    FName VARCHAR(20),
    LName VARCHAR(20),
    DOB CHAR(10),
    Major VARCHAR(20),
    PRIMARY KEY(StudentId)
);

CREATE TABLE Phone
(
    sID INTEGER,
    Pnumber CHAR(20),
    Type CHAR(3),
    PRIMARY KEY(Pnumber)
);

CREATE TABLE Class
(
    ClassId VARCHAR(6),
    Description VARCHAR(30),
    NumCredits Integer,
    Prereq VARCHAR(20),
    PRIMARY KEY(ClassId)
);

CREATE TABLE Section
(
    ClassId VARCHAR(6),
    SecNo CHAR(10),
    Semester CHAR(4),
    ClassRoom VARCHAR(6),
    TimeOffered VARCHAR(18),
    PRIMARY KEY(SecNo),
    FOREIGN KEY(ClassId) REFERENCES Class(ClassId)  
);

CREATE TABLE Enrolled
(
    StudentId INTEGER,
    SecNum VARCHAR(40),
    ClassId VARCHAR(8),
    Semes VARCHAR(6),
    GorDD VARCHAR(30)
    FOREIGN KEY(ClassId) REFERENCES Section(ClassId),
    FOREIGN KEY(StudentId) REFERENCES Student(StudentId)
);

CREATE TABLE Professor
(
    EmpId INTEGER,
    FName VARCHAR(10),
    LName VARCHAR(10),
    Dept VARCHAR(2),
    QualClass VARCHAR(40),
    PRIMARY KEY (EmpId)
);

CREATE TABLE Teaches
(
    Class VARCHAR(5),
    Section INTEGER,
    Semester CHAR(4),
    EmpId INTEGER,
    FOREIGN KEY (EmpId) REFERENCES Professor(EmpId)
);

CREATE TABLE Qualified
(
    EmpId INTEGER,
    ClassId VARCHAR(5)
);

############################# odd/even

DO $$
DECLARE
   a integer := 7;
BEGIN 
  IF a%2 = 0 THEN 
     RAISE NOTICE 'Integer is even';
  ELSE
     RAISE NOTICE 'Integer is odd';
  END IF;
END $$;

############################# factorial

do $$ 
declare
fac integer :=1;
n integer := 5;

begin		
while n > 0 loop
fac:=n*fac;		
n:=n-1;		
end loop;		

raise notice 'Value: %', fac;

end $$;

############################# Sum of n integers

do $$ 
DECLARE 
  x integer; 
  n integer:=4; 
  i integer; 
  sums integer :=0 ;

BEGIN 
  while n>0 loop
    sums := sums + n; 
    n:=n-1;
END LOOP; 

raise notice'Sum: % ' ,sums; 

end $$;
