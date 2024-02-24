# TASK 3 - Secure Coding Review
Choose a programming language and application. Review the code for security vulnerabilities and provide recommendations for secure coding practices.<br>
Use tools like static code analyzers or manual code review.

This is a Project I made as a part of Course Work<br>
Performing a Secure code review on this application to find and fix its vulnerabilities.<br>
Project Link - [ADS - IOT](https://github.com/DPRIYATHAM/ADS-IOT/tree/main/Software)

> Securing an application is as Important as Building the Application.

Let's Hear About Secure Coding from `OWASP`

Source code analysis tools, also known as Static Application Security Testing (SAST) Tools, can help analyze source code or compiled versions of code to help find security flaws. (WhiteBox Testing)

SAST tools can be added to your IDE. Such tools can help you detect issues during software development. SAST tool feedback can save time and effort, especially when compared to finding vulnerabilities later in the development cycle

## SAST - Important Selection Criteria
- Prerequisite: Support your programming language.
- Ability to detect vulnerabilities, based on:
    - [The OWASP Top Ten](https://owasp.org/www-project-top-ten/)
    - Other criteria such as:
        - [OSSTMM](https://www.isecom.org/OSSTMM.3.pdf)
        - [CHECK](https://www.ncsc.gov.uk/information/check-penetration-testing)
- Accuracy:
    - False Positive/False Negative rates
- OWASP Benchmark score
- Ability to understand the libraries/frameworks you need
- Requirement for buildable source code
- Ability to run against binaries (instead of source)
- Availability as a plugin into preferred developer IDEs
- Ease of setup/use
- Ability to include in Continuous Integration/Deployment tools
- License cost (May vary by user, organization, app, or lines of code)
- Interoperability of output:
- See OASIS SARIF (Static Analysis Results Interchange Format)
- Static Code Analysis - [Link](https://owasp.org/www-community/controls/Static_Code_Analysis)
- These are some tools we can use to perform Secure Coding Analysis - 
    - [OWASP - Source Code Analysis Tools](https://owasp.org/www-community/Source_Code_Analysis_Tools)
    - [NIST - Source Code Security Analyzers](http://samate.nist.gov/index.php/Source_Code_Security_Analyzers.html)
    - [Wikipedia - List of tools for static code analysis](https://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis)
- OWASP Project Benchmarks - [Link](https://owasp.org/www-project-benchmark/)

According to My Project, I found these Tools useful and I am exploring them.
- ASH by AWS - Open Source, Free - [Link](https://github.com/awslabs/automated-security-helper)
- Bandit - Open Source - [Link](https://github.com/PyCQA/bandit)
- HCL AppScan - Open Source, Free - [Link](https://github.com/marketplace/actions/hcl-appscan-codesweep)
- Pyre - Open Source, Free - [Link](https://pyre-check.org/)
- Veracode - Open Source, Free - [Link](https://www.veracode.com/)

> Through the Manual Secure Coding Review of My Application I followed OWASP's Top Ten

- Fixed the Broken Access Control - Using JWT Token
- Fixed the Cryptographic Failures - By Applying Encryption to the Data in the DataBase
- Working on other Vulnerabilities too.
- As a part of this Internship Program I have worked on these as of now.
- I will be continuing to work on these even after the Internship period (driven by passion)

## Conclusion
This is a great experience to learn Secure Coding Review and to correct the mistakes I made as a developer before.
