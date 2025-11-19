// DOM Elements
const loginForm = document.getElementById('login-form');
const signupForm = document.getElementById('signup-form');
const authContainer = document.getElementById('auth-container');
const appContainer = document.getElementById('app-container');
const logoutContainer = document.getElementById('logout-container');
const rightHoverArea = document.getElementById('right-hover-area');
const logoutButton = document.getElementById('logout-button');
const resumeUpload = document.getElementById('resume-upload');
const uploadLabel = document.getElementById('upload-label');
const fileName = document.getElementById('file-name');
const analyzeButton = document.getElementById('analyze-button');
const skillsContainer = document.getElementById('extracted-skills');
const resumeFeedback = document.getElementById('resume-feedback');
const skillsDashboard = document.getElementById('skills-dashboard');

// Tab Navigation
function setupTabs() {
    // Auth tabs
    const authTabBtns = document.querySelectorAll('.auth-tab-btn');
    const authTabContents = document.querySelectorAll('.auth-tab-content');
    
    authTabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const tabId = btn.getAttribute('data-tab');
            
            // Update active tab button
            authTabBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            // Show active tab content
            authTabContents.forEach(content => {
                if (content.getAttribute('id') === tabId) {
                    content.classList.add('active');
                } else {
                    content.classList.remove('active');
                }
            });
        });
    });
    
    // Main app tabs
    const appTabLinks = document.querySelectorAll('.nav-link');
    const appTabContents = document.querySelectorAll('.tab-pane');
    
    appTabLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const tabId = link.getAttribute('href').substring(1);
            
            // Update active tab link
            appTabLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
            
            // Show active tab content
            appTabContents.forEach(content => {
                if (content.getAttribute('id') === tabId) {
                    content.classList.add('active', 'show');
                } else {
                    content.classList.remove('active', 'show');
                }
            });
        });
    });
    
    // Career advisor sub-tabs
    const careerSubTabLinks = document.querySelectorAll('.career-subtab-link');
    const careerSubTabContents = document.querySelectorAll('.career-subtab-content');
    
    careerSubTabLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const tabId = link.getAttribute('href').substring(1);
            
            // Update active tab link
            careerSubTabLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
            
            // Show active tab content
            careerSubTabContents.forEach(content => {
                if (content.getAttribute('id') === tabId) {
                    content.classList.add('active', 'show');
                } else {
                    content.classList.remove('active', 'show');
                }
            });
        });
    });
    
    // Interview prep sub-tabs
    const interviewSubTabLinks = document.querySelectorAll('.interview-subtab-link');
    const interviewSubTabContents = document.querySelectorAll('.interview-subtab-content');
    
    interviewSubTabLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const tabId = link.getAttribute('href').substring(1);
            
            // Update active tab link
            interviewSubTabLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
            
            // Show active tab content
            interviewSubTabContents.forEach(content => {
                if (content.getAttribute('id') === tabId) {
                    content.classList.add('active', 'show');
                } else {
                    content.classList.remove('active', 'show');
                }
            });
        });
    });
}

// Expandable Sections
function setupExpandableSections() {
    const expandableHeaders = document.querySelectorAll('.expandable-header');
    
    expandableHeaders.forEach(header => {
        header.addEventListener('click', () => {
            const content = header.nextElementSibling;
            content.classList.toggle('active');
            
            // Update icon
            const icon = header.querySelector('i');
            if (content.classList.contains('active')) {
                icon.classList.remove('fa-chevron-down');
                icon.classList.add('fa-chevron-up');
            } else {
                icon.classList.remove('fa-chevron-up');
                icon.classList.add('fa-chevron-down');
            }
        });
    });
}

// Logout Button Hover Effect
function setupLogoutButton() {
    if (rightHoverArea && logoutContainer) {
        rightHoverArea.addEventListener('mouseenter', () => {
            logoutContainer.style.opacity = '1';
        });
        
        rightHoverArea.addEventListener('mouseleave', () => {
            logoutContainer.style.opacity = '0.2';
        });
        
        logoutButton.addEventListener('click', () => {
            // Show auth container, hide app container
            authContainer.style.display = 'block';
            appContainer.style.display = 'none';
            logoutContainer.style.display = 'none';
            
            // Reset forms
            if (loginForm) loginForm.reset();
            if (signupForm) signupForm.reset();
        });
    }
}

// File Upload Handling
function setupFileUpload() {
    if (resumeUpload && uploadLabel && fileName) {
        resumeUpload.addEventListener('change', (e) => {
            if (e.target.files.length > 0) {
                const file = e.target.files[0];
                fileName.textContent = file.name;
                analyzeButton.disabled = false;
            } else {
                fileName.textContent = 'No file selected';
                analyzeButton.disabled = true;
            }
        });
        
        analyzeButton.addEventListener('click', () => {
            if (resumeUpload.files.length > 0) {
                // Simulate file processing
                analyzeButton.disabled = true;
                analyzeButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';
                
                setTimeout(() => {
                    analyzeResume(resumeUpload.files[0]);
                    analyzeButton.innerHTML = 'Analyze Resume';
                    analyzeButton.disabled = false;
                }, 2000);
            }
        });
    }
}

// Mock Resume Analysis
function analyzeResume(file) {
    // Mock extracted skills
    const mockSkills = {
        technical: ['Python', 'JavaScript', 'React', 'Node.js', 'SQL', 'Data Analysis', 'Machine Learning'],
        soft: ['Communication', 'Teamwork', 'Problem Solving', 'Leadership'],
        domain: ['Finance', 'Healthcare', 'E-commerce']
    };
    
    // Display extracted skills
    displayExtractedSkills(mockSkills);
    
    // Display resume feedback
    displayResumeFeedback();
    
    // Display skills dashboard
    displaySkillsDashboard(mockSkills);
    
    // Show results containers
    document.getElementById('results-container').style.display = 'block';
    document.getElementById('skills-dashboard-container').style.display = 'block';
}

// Display Extracted Skills
function displayExtractedSkills(skills) {
    if (skillsContainer) {
        skillsContainer.innerHTML = '';
        
        // Technical Skills
        const technicalSection = document.createElement('div');
        technicalSection.className = 'mb-4';
        technicalSection.innerHTML = `
            <h4 class="mb-3">Technical Skills</h4>
            <div class="d-flex flex-wrap">
                ${skills.technical.map(skill => `
                    <span class="badge bg-primary m-1 p-2">${skill}</span>
                `).join('')}
            </div>
        `;
        skillsContainer.appendChild(technicalSection);
        
        // Soft Skills
        const softSection = document.createElement('div');
        softSection.className = 'mb-4';
        softSection.innerHTML = `
            <h4 class="mb-3">Soft Skills</h4>
            <div class="d-flex flex-wrap">
                ${skills.soft.map(skill => `
                    <span class="badge bg-success m-1 p-2">${skill}</span>
                `).join('')}
            </div>
        `;
        skillsContainer.appendChild(softSection);
        
        // Domain Skills
        const domainSection = document.createElement('div');
        domainSection.className = 'mb-4';
        domainSection.innerHTML = `
            <h4 class="mb-3">Domain Knowledge</h4>
            <div class="d-flex flex-wrap">
                ${skills.domain.map(skill => `
                    <span class="badge bg-info m-1 p-2">${skill}</span>
                `).join('')}
            </div>
        `;
        skillsContainer.appendChild(domainSection);
    }
}

// Display Resume Feedback
function displayResumeFeedback() {
    if (resumeFeedback) {
        resumeFeedback.innerHTML = `
            <div class="alert alert-primary">
                <h4 class="alert-heading">Overall Assessment</h4>
                <p>Your resume demonstrates strong technical skills and relevant experience. Here are some suggestions for improvement:</p>
            </div>
            
            <div class="expandable-section">
                <div class="expandable-header">
                    <h5>Strengths</h5>
                    <i class="fas fa-chevron-down"></i>
                </div>
                <div class="expandable-content">
                    <ul>
                        <li>Strong technical skill set with in-demand technologies</li>
                        <li>Clear project descriptions with measurable outcomes</li>
                        <li>Good balance of technical and soft skills</li>
                    </ul>
                </div>
            </div>
            
            <div class="expandable-section">
                <div class="expandable-header">
                    <h5>Areas for Improvement</h5>
                    <i class="fas fa-chevron-down"></i>
                </div>
                <div class="expandable-content">
                    <ul>
                        <li>Consider adding more quantifiable achievements</li>
                        <li>Tailor your resume more specifically to your target roles</li>
                        <li>Add more keywords relevant to job descriptions in your field</li>
                    </ul>
                </div>
            </div>
            
            <div class="expandable-section">
                <div class="expandable-header">
                    <h5>Suggested Edits</h5>
                    <i class="fas fa-chevron-down"></i>
                </div>
                <div class="expandable-content">
                    <ul>
                        <li>Reorganize skills section to highlight most relevant technologies first</li>
                        <li>Add a brief professional summary at the top</li>
                        <li>Include metrics and results for each role (e.g., "Increased efficiency by 30%")</li>
                    </ul>
                </div>
            </div>
        `;
        
        // Setup expandable sections
        setupExpandableSections();
    }
}

// Display Skills Dashboard
function displaySkillsDashboard(skills) {
    if (skillsDashboard) {
        // Create skill category distribution chart
        const categoryCtx = document.getElementById('skill-category-chart');
        if (categoryCtx) {
            new Chart(categoryCtx, {
                type: 'pie',
                data: {
                    labels: ['Technical', 'Soft', 'Domain'],
                    datasets: [{
                        data: [skills.technical.length, skills.soft.length, skills.domain.length],
                        backgroundColor: ['#0f62fe', '#24a148', '#1192e8']
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'bottom'
                        },
                        title: {
                            display: true,
                            text: 'Skill Category Distribution'
                        }
                    }
                }
            });
        }
        
        // Create skill coverage radar chart
        const coverageCtx = document.getElementById('skill-coverage-chart');
        if (coverageCtx) {
            new Chart(coverageCtx, {
                type: 'radar',
                data: {
                    labels: ['Programming', 'Data Analysis', 'Web Development', 'Soft Skills', 'Domain Knowledge'],
                    datasets: [{
                        label: 'Your Skills',
                        data: [85, 70, 80, 75, 60],
                        backgroundColor: 'rgba(15, 98, 254, 0.2)',
                        borderColor: '#0f62fe',
                        pointBackgroundColor: '#0f62fe'
                    }, {
                        label: 'Industry Average',
                        data: [70, 65, 75, 60, 70],
                        backgroundColor: 'rgba(36, 161, 72, 0.2)',
                        borderColor: '#24a148',
                        pointBackgroundColor: '#24a148'
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'bottom'
                        },
                        title: {
                            display: true,
                            text: 'Skill Coverage Analysis'
                        }
                    },
                    scales: {
                        r: {
                            min: 0,
                            max: 100,
                            ticks: {
                                stepSize: 20
                            }
                        }
                    }
                }
            });
        }
    }
}

// Job Search Functions
function setupJobSearch() {
    const findJobsButton = document.getElementById('find-jobs-button');
    if (findJobsButton) {
        findJobsButton.addEventListener('click', () => {
            // Simulate job search
            findJobsButton.disabled = true;
            findJobsButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Searching...';
            
            setTimeout(() => {
                searchJobs();
                findJobsButton.innerHTML = 'Find Jobs';
                findJobsButton.disabled = false;
            }, 2000);
        });
    }
}

// Mock Job Search
function searchJobs() {
    // Mock job data
    const mockJobs = [
        {
            title: 'Senior Software Engineer',
            company: 'IBM',
            location: 'New York, NY',
            salary: '$120,000 - $150,000',
            posted: '2 days ago',
            match: 92,
            description: 'We are looking for a Senior Software Engineer with expertise in Python, React, and Node.js to join our team...',
            requirements: ['5+ years of experience', 'Python', 'React', 'Node.js', 'SQL', 'Cloud platforms'],
            companySize: 'Large (10,000+ employees)',
            jobType: 'Full-time'
        },
        {
            title: 'Data Scientist',
            company: 'Microsoft',
            location: 'Seattle, WA',
            salary: '$110,000 - $140,000',
            posted: '1 week ago',
            match: 85,
            description: 'Join our data science team to build machine learning models and analyze large datasets...',
            requirements: ['3+ years of experience', 'Python', 'Machine Learning', 'Data Analysis', 'SQL', 'Statistics'],
            companySize: 'Large (10,000+ employees)',
            jobType: 'Full-time'
        },
        {
            title: 'Frontend Developer',
            company: 'Google',
            location: 'Mountain View, CA',
            salary: '$100,000 - $130,000',
            posted: '3 days ago',
            match: 78,
            description: 'We are seeking a talented Frontend Developer to create responsive and interactive web applications...',
            requirements: ['2+ years of experience', 'JavaScript', 'React', 'HTML/CSS', 'UI/UX', 'Testing'],
            companySize: 'Large (10,000+ employees)',
            jobType: 'Full-time'
        },
        {
            title: 'Full Stack Developer',
            company: 'Amazon',
            location: 'Remote',
            salary: '$95,000 - $125,000',
            posted: '5 days ago',
            match: 80,
            description: 'Looking for a Full Stack Developer to work on our e-commerce platform...',
            requirements: ['3+ years of experience', 'JavaScript', 'Node.js', 'React', 'MongoDB', 'AWS'],
            companySize: 'Large (10,000+ employees)',
            jobType: 'Full-time'
        },
        {
            title: 'Machine Learning Engineer',
            company: 'Netflix',
            location: 'Los Angeles, CA',
            salary: '$130,000 - $160,000',
            posted: '1 day ago',
            match: 75,
            description: 'Join our ML team to develop recommendation algorithms and personalization features...',
            requirements: ['4+ years of experience', 'Python', 'Machine Learning', 'Deep Learning', 'TensorFlow/PyTorch', 'Big Data'],
            companySize: 'Large (5,000+ employees)',
            jobType: 'Full-time'
        }
    ];
    
    // Display job results
    displayJobResults(mockJobs);
    
    // Show job results container
    document.getElementById('job-results-container').style.display = 'block';
}

// Display Job Results
function displayJobResults(jobs) {
    const jobResultsContainer = document.getElementById('job-results');
    if (jobResultsContainer) {
        jobResultsContainer.innerHTML = '';
        
        jobs.forEach(job => {
            const jobCard = document.createElement('div');
            jobCard.className = 'expandable-section job-card';
            jobCard.innerHTML = `
                <div class="expandable-header">
                    <div>
                        <h4>${job.title}</h4>
                        <p>${job.company} - ${job.location}</p>
                    </div>
                    <div class="d-flex align-items-center">
                        <span class="badge bg-primary me-3">${job.match}% Match</span>
                        <i class="fas fa-chevron-down"></i>
                    </div>
                </div>
                <div class="expandable-content">
                    <div class="row mb-3">
                        <div class="col-md-6">
                            <p><strong>Salary:</strong> ${job.salary}</p>
                            <p><strong>Posted:</strong> ${job.posted}</p>
                        </div>
                        <div class="col-md-6">
                            <p><strong>Company Size:</strong> ${job.companySize}</p>
                            <p><strong>Job Type:</strong> ${job.jobType}</p>
                        </div>
                    </div>
                    
                    <div class="mb-3">
                        <h5>Job Description</h5>
                        <p>${job.description}</p>
                    </div>
                    
                    <div class="mb-3">
                        <h5>Requirements</h5>
                        <ul>
                            ${job.requirements.map(req => `<li>${req}</li>`).join('')}
                        </ul>
                    </div>
                    
                    <div class="d-flex justify-content-between">
                        <button class="btn btn-primary save-job-btn" data-job-title="${job.title}" data-job-company="${job.company}">
                            <i class="fas fa-bookmark"></i> Save Job
                        </button>
                        <button class="btn btn-outline-primary">
                            <i class="fas fa-external-link-alt"></i> Apply Now
                        </button>
                    </div>
                </div>
            `;
            
            jobResultsContainer.appendChild(jobCard);
        });
        
        // Setup expandable sections for job cards
        setupExpandableSections();
        
        // Setup save job buttons
        setupSaveJobButtons();
    }
}

// Setup Save Job Buttons
function setupSaveJobButtons() {
    const saveJobButtons = document.querySelectorAll('.save-job-btn');
    const savedJobsList = document.getElementById('saved-jobs-list');
    
    if (saveJobButtons && savedJobsList) {
        saveJobButtons.forEach(button => {
            button.addEventListener('click', () => {
                const jobTitle = button.getAttribute('data-job-title');
                const jobCompany = button.getAttribute('data-job-company');
                
                // Add to saved jobs list
                const savedJob = document.createElement('div');
                savedJob.className = 'saved-job-item p-3 border-bottom';
                savedJob.innerHTML = `
                    <div class="d-flex justify-content-between align-items-center">
                        <div>
                            <h5 class="mb-1">${jobTitle}</h5>
                            <p class="mb-0">${jobCompany}</p>
                        </div>
                        <div>
                            <select class="form-select form-select-sm application-status">
                                <option value="Saved">Saved</option>
                                <option value="Applied">Applied</option>
                                <option value="Interviewing">Interviewing</option>
                                <option value="Offered">Offered</option>
                                <option value="Rejected">Rejected</option>
                            </select>
                        </div>
                    </div>
                `;
                
                savedJobsList.appendChild(savedJob);
                
                // Show saved jobs container
                document.getElementById('saved-jobs-container').style.display = 'block';
                
                // Disable the save button
                button.disabled = true;
                button.innerHTML = '<i class="fas fa-check"></i> Saved';
            });
        });
    }
}

// Career Advisor Functions
function setupCareerAdvisor() {
    const generateAdviceButton = document.getElementById('generate-advice-button');
    if (generateAdviceButton) {
        generateAdviceButton.addEventListener('click', () => {
            // Simulate generating career advice
            generateAdviceButton.disabled = true;
            generateAdviceButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Generating...';
            
            setTimeout(() => {
                generateCareerAdvice();
                generateAdviceButton.innerHTML = 'Generate Advice';
                generateAdviceButton.disabled = false;
            }, 2000);
        });
    }
}

// Mock Career Advice Generation
function generateCareerAdvice() {
    // Display career advice
    displayCareerAdvice();
    
    // Show career advice container
    document.getElementById('career-advice-container').style.display = 'block';
}

// Display Career Advice
function displayCareerAdvice() {
    // Overview section
    const overviewContainer = document.getElementById('career-overview');
    if (overviewContainer) {
        overviewContainer.innerHTML = `
            <div class="alert alert-primary">
                <h4 class="alert-heading">Career Path Overview</h4>
                <p>Based on your skills and preferences, you're well-positioned for roles in software development with a focus on full-stack development. Your technical skills in Python, JavaScript, and React are highly marketable, and your soft skills complement your technical abilities well.</p>
            </div>
            
            <div class="row">
                <div class="col-md-6">
                    <div class="card mb-4">
                        <div class="card-header bg-primary text-white">
                            <h5 class="mb-0">Strengths</h5>
                        </div>
                        <div class="card-body">
                            <ul>
                                <li>Strong technical foundation in modern web technologies</li>
                                <li>Balance of frontend and backend skills</li>
                                <li>Problem-solving and communication abilities</li>
                            </ul>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-6">
                    <div class="card mb-4">
                        <div class="card-header bg-primary text-white">
                            <h5 class="mb-0">Areas for Growth</h5>
                        </div>
                        <div class="card-body">
                            <ul>
                                <li>Cloud infrastructure and DevOps practices</li>
                                <li>Advanced data structures and algorithms</li>
                                <li>Leadership and project management</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }
    
    // Career paths section
    const careerPathsContainer = document.getElementById('career-paths');
    if (careerPathsContainer) {
        careerPathsContainer.innerHTML = `
            <div class="row">
                <div class="col-md-4 mb-4">
                    <div class="card h-100">
                        <div class="card-header bg-primary text-white">
                            <h5 class="mb-0">Full Stack Developer</h5>
                            <span class="badge bg-light text-primary">95% Match</span>
                        </div>
                        <div class="card-body">
                            <p>Develop both frontend and backend components of web applications using your existing skills in JavaScript, React, and Node.js.</p>
                            <h6>Key Skills:</h6>
                            <div class="d-flex flex-wrap mb-3">
                                <span class="badge bg-primary m-1">JavaScript</span>
                                <span class="badge bg-primary m-1">React</span>
                                <span class="badge bg-primary m-1">Node.js</span>
                                <span class="badge bg-primary m-1">SQL</span>
                                <span class="badge bg-primary m-1">REST APIs</span>
                            </div>
                            <h6>Growth Trajectory:</h6>
                            <p>Senior Developer → Lead Developer → Technical Architect</p>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-4 mb-4">
                    <div class="card h-100">
                        <div class="card-header bg-primary text-white">
                            <h5 class="mb-0">Data Engineer</h5>
                            <span class="badge bg-light text-primary">85% Match</span>
                        </div>
                        <div class="card-body">
                            <p>Build data pipelines and infrastructure to collect, process, and analyze large datasets, leveraging your Python and SQL skills.</p>
                            <h6>Key Skills:</h6>
                            <div class="d-flex flex-wrap mb-3">
                                <span class="badge bg-primary m-1">Python</span>
                                <span class="badge bg-primary m-1">SQL</span>
                                <span class="badge bg-primary m-1">ETL</span>
                                <span class="badge bg-primary m-1">Data Modeling</span>
                                <span class="badge bg-primary m-1">Cloud Platforms</span>
                            </div>
                            <h6>Growth Trajectory:</h6>
                            <p>Senior Data Engineer → Data Architect → Director of Data Engineering</p>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-4 mb-4">
                    <div class="card h-100">
                        <div class="card-header bg-primary text-white">
                            <h5 class="mb-0">DevOps Engineer</h5>
                            <span class="badge bg-light text-primary">75% Match</span>
                        </div>
                        <div class="card-body">
                            <p>Implement CI/CD pipelines and manage cloud infrastructure to streamline software development and deployment processes.</p>
                            <h6>Key Skills:</h6>
                            <div class="d-flex flex-wrap mb-3">
                                <span class="badge bg-primary m-1">Cloud Platforms</span>
                                <span class="badge bg-primary m-1">CI/CD</span>
                                <span class="badge bg-primary m-1">Docker</span>
                                <span class="badge bg-primary m-1">Kubernetes</span>
                                <span class="badge bg-primary m-1">Infrastructure as Code</span>
                            </div>
                            <h6>Growth Trajectory:</h6>
                            <p>Senior DevOps Engineer → DevOps Architect → Cloud Infrastructure Manager</p>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }
    
    // Skill development section
    const skillDevelopmentContainer = document.getElementById('skill-development');
    if (skillDevelopmentContainer) {
        skillDevelopmentContainer.innerHTML = `
            <div class="row">
                <div class="col-md-4 mb-4">
                    <div class="card h-100">
                        <div class="card-header bg-success text-white">
                            <h5 class="mb-0">Short-term (3-6 months)</h5>
                        </div>
                        <div class="card-body">
                            <ul class="list-group list-group-flush">
                                <li class="list-group-item">
                                    <h6>Advanced React Patterns</h6>
                                    <p class="mb-0">Learn context API, hooks, and performance optimization techniques</p>
                                </li>
                                <li class="list-group-item">
                                    <h6>API Design</h6>
                                    <p class="mb-0">Master RESTful API design principles and GraphQL</p>
                                </li>
                                <li class="list-group-item">
                                    <h6>Testing Strategies</h6>
                                    <p class="mb-0">Implement unit, integration, and end-to-end testing</p>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-4 mb-4">
                    <div class="card h-100">
                        <div class="card-header bg-warning text-dark">
                            <h5 class="mb-0">Medium-term (6-12 months)</h5>
                        </div>
                        <div class="card-body">
                            <ul class="list-group list-group-flush">
                                <li class="list-group-item">
                                    <h6>Cloud Certification</h6>
                                    <p class="mb-0">Obtain AWS, Azure, or GCP certification</p>
                                </li>
                                <li class="list-group-item">
                                    <h6>Containerization & Orchestration</h6>
                                    <p class="mb-0">Learn Docker and Kubernetes fundamentals</p>
                                </li>
                                <li class="list-group-item">
                                    <h6>Advanced Data Structures</h6>
                                    <p class="mb-0">Strengthen algorithm design and problem-solving skills</p>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-4 mb-4">
                    <div class="card h-100">
                        <div class="card-header bg-danger text-white">
                            <h5 class="mb-0">Long-term (1-2 years)</h5>
                        </div>
                        <div class="card-body">
                            <ul class="list-group list-group-flush">
                                <li class="list-group-item">
                                    <h6>System Design</h6>
                                    <p class="mb-0">Master designing scalable, distributed systems</p>
                                </li>
                                <li class="list-group-item">
                                    <h6>Leadership Skills</h6>
                                    <p class="mb-0">Develop project management and team leadership abilities</p>
                                </li>
                                <li class="list-group-item">
                                    <h6>Specialized Domain Knowledge</h6>
                                    <p class="mb-0">Deepen expertise in a specific industry vertical</p>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }
    
    // Learning resources section
    const learningResourcesContainer = document.getElementById('learning-resources');
    if (learningResourcesContainer) {
        learningResourcesContainer.innerHTML = `
            <div class="mb-4">
                <div class="input-group">
                    <input type="text" class="form-control" placeholder="Search resources..." id="resource-search">
                    <button class="btn btn-outline-primary" type="button">Search</button>
                </div>
            </div>
            
            <div class="table-responsive">
                <table class="table table-hover">
                    <thead class="table-light">
                        <tr>
                            <th>Resource</th>
                            <th>Type</th>
                            <th>Topic</th>
                            <th>Cost</th>
                            <th>Time</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Advanced React Patterns</td>
                            <td>Course</td>
                            <td>Frontend</td>
                            <td>$79</td>
                            <td>10 hours</td>
                            <td><button class="btn btn-sm btn-outline-primary">View</button></td>
                        </tr>
                        <tr>
                            <td>System Design Interview</td>
                            <td>Book</td>
                            <td>Architecture</td>
                            <td>$35</td>
                            <td>20 hours</td>
                            <td><button class="btn btn-sm btn-outline-primary">View</button></td>
                        </tr>
                        <tr>
                            <td>AWS Certified Solutions Architect</td>
                            <td>Certification</td>
                            <td>Cloud</td>
                            <td>$150</td>
                            <td>80 hours</td>
                            <td><button class="btn btn-sm btn-outline-primary">View</button></td>
                        </tr>
                        <tr>
                            <td>Algorithms Specialization</td>
                            <td>Course</td>
                            <td>Computer Science</td>
                            <td>Free</td>
                            <td>40 hours</td>
                            <td><button class="btn btn-sm btn-outline-primary">View</button></td>
                        </tr>
                        <tr>
                            <td>Docker & Kubernetes: The Complete Guide</td>
                            <td>Course</td>
                            <td>DevOps</td>
                            <td>$89</td>
                            <td>30 hours</td>
                            <td><button class="btn btn-sm btn-outline-primary">View</button></td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
            <div class="mt-4">
                <h5>Industry Trends</h5>
                <div class="alert alert-info">
                    <p><strong>Full Stack Development:</strong> Increasing demand for developers who can work across the entire stack, with emphasis on JavaScript frameworks and cloud services.</p>
                    <p><strong>DevOps & Cloud:</strong> Growing adoption of containerization, microservices architecture, and serverless computing.</p>
                    <p><strong>AI & Machine Learning:</strong> Integration of AI capabilities into traditional software applications becoming more common.</p>
                </div>
            </div>
        `;
    }
    
    // Career dashboard section
    const careerDashboardContainer = document.getElementById('career-dashboard');
    if (careerDashboardContainer) {
        // Create career path compatibility chart
        const pathCtx = document.getElementById('career-path-chart');
        if (pathCtx) {
            new Chart(pathCtx, {
                type: 'bar',
                data: {
                    labels: ['Full Stack Developer', 'Data Engineer', 'DevOps Engineer', 'Frontend Specialist', 'Backend Specialist'],
                    datasets: [{
                        label: 'Compatibility',
                        data: [95, 85, 75, 90, 88],
                        backgroundColor: '#0f62fe'
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            display: false
                        },
                        title: {
                            display: true,
                            text: 'Career Path Compatibility'
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 100,
                            title: {
                                display: true,
                                text: 'Match Percentage'
                            }
                        }
                    }
                }
            });
        }
        
        // Create work preferences radar chart
        const preferencesCtx = document.getElementById('work-preferences-chart');
        if (preferencesCtx) {
            new Chart(preferencesCtx, {
                type: 'radar',
                data: {
                    labels: ['Remote Work', 'Work-Life Balance', 'Learning Opportunities', 'Compensation', 'Company Culture'],
                    datasets: [{
                        label: 'Your Preferences',
                        data: [90, 85, 95, 80, 85],
                        backgroundColor: 'rgba(15, 98, 254, 0.2)',
                        borderColor: '#0f62fe',
                        pointBackgroundColor: '#0f62fe'
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            display: false
                        },
                        title: {
                            display: true,
                            text: 'Work Preferences Analysis'
                        }
                    },
                    scales: {
                        r: {
                            min: 0,
                            max: 100,
                            ticks: {
                                stepSize: 20
                            }
                        }
                    }
                }
            });
        }
    }
}

// Initialize Application
document.addEventListener('DOMContentLoaded', () => {
    // Setup tabs
    setupTabs();
    
    // Setup logout button
    setupLogoutButton();
    
    // Setup file upload
    setupFileUpload();
    
    // Setup job search
    setupJobSearch();
    
    // Setup career advisor
    setupCareerAdvisor();
    
    // Auth form submission
    const loginForm = document.getElementById('login-form');
    const signupForm = document.getElementById('signup-form');
    
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            // Simulate login
            const email = document.getElementById('login-email').value;
            const password = document.getElementById('login-password').value;
            
            if (email && password) {
                // Show app container, hide auth container
                authContainer.style.display = 'none';
                appContainer.style.display = 'block';
                logoutContainer.style.display = 'block';
            }
        });
    }
    
    if (signupForm) {
        signupForm.addEventListener('submit', (e) => {
            e.preventDefault();
            // Simulate signup
            const name = document.getElementById('signup-name').value;
            const email = document.getElementById('signup-email').value;
            const password = document.getElementById('signup-password').value;
            
            if (name && email && password) {
                // Show app container, hide auth container
                authContainer.style.display = 'none';
                appContainer.style.display = 'block';
                logoutContainer.style.display = 'block';
            }
        });
    }
});