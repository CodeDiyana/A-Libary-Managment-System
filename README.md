<h1>Libary Managment System</h1>




<h2>Description</h2>
Implementation Overview
The Library management system was created using four classes, Book, Member, StudentMember, TeacherMember and Library which is a representation of all the four pillars of OOP (encapsulation, inheritance, polymorphism and abstraction).






<h2>OOP Concepts Used:</h2>







Created classes like Book, Member, and Library to model real-world library entities.




Inheritance & Polymorphism






Encapsulation & Data Hiding











 
<h2>Program walk-through:</h2>



<p align="center">
<br /> 
Classes and Objects: Book This is a library resource whose attribute contains a set of information such as an ID, title, author, current borrower and status of availability. Member Library Users Member is the parent of the library users that has a member id, name and an internal array of books borrowed (Alexander, 2022). The central management class is that which keeps collection of books and members in the library.
 
 <br />Encapsulation and Data Hiding: The Member class has a name-mangled private attribute: The borrowed books which is used to make direct access by the outsider to a borrowing list of the member. The Library class is no exception as it secures its collection of books and members, as well. All access to these private attributes is done via specified public functions like borrow book, return book and access to these attributes is controlled and data integrity is provided. Availability of books is merely the option of these validated procedures instead of the immediate change or manipulation of attributes . 

<br/> Inheritance and Polymorphism: StudentsMember and TeacherMember inherits UserMember which is extended with role specific attributes. The studentMember has a limit of borrow 3 and student-id, and the TeacherMember has a limit of borrow 10. This hierarchy reflects the real world policies and has different user roles with different borrowing privileges, the polymorphic behaviour is reflected with specialised subclass attributes and share the same borrowing interface with the parent one .<br/>

<h2>Disscusion:</h2>

The system plays well in lifecycle management in book borrowing and giving back. Encapsulation is used to make sure that the availability of the books cannot be changed without going through the borrow book and the return book method which consists of validations (e.g. is the book really available before the book is borrowed). The hereditance system is pure and expandable System - It was easy to add other types of members (e.g., GuestMember) into the structure as subclasses of Member without making any changes to the main program, which is in line with the Open/Closed Principle. The system demonstrates how OOP reveals the real-life objects in their inherent state, and how the code is user- and service-friendly.
