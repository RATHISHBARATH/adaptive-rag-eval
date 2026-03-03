export interface Assessment {
  name: string;
  test_type: string[];
  duration: number;
  adaptive_support: string;
  remote_support: string;
  description: string;
  url: string;
}

export interface HistoryItem {
  id: string;
  query: string;
  timestamp: string;
  resultCount: number;
  results: Assessment[];
}

export const MOCK_ASSESSMENTS: Assessment[] = [
  {
    name: "Verify Interactive - Python Programming",
    test_type: ["Knowledge & Skills"],
    duration: 30,
    adaptive_support: "Yes",
    remote_support: "Yes",
    description: "Assesses Python programming proficiency including data structures, algorithms, OOP concepts, library usage, and problem-solving for mid to senior-level developers.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Verify Interactive - SQL & Databases",
    test_type: ["Knowledge & Skills"],
    duration: 25,
    adaptive_support: "Yes",
    remote_support: "Yes",
    description: "Evaluates SQL skills including complex queries, joins, subqueries, database design, normalization, indexing, and performance optimization.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Verify Interactive - JavaScript",
    test_type: ["Knowledge & Skills"],
    duration: 30,
    adaptive_support: "Yes",
    remote_support: "Yes",
    description: "Assesses JavaScript proficiency covering ES6+, closures, prototypes, async/await, DOM manipulation, and modern framework concepts.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Verify Interactive - Java Enterprise",
    test_type: ["Knowledge & Skills"],
    duration: 35,
    adaptive_support: "Yes",
    remote_support: "Yes",
    description: "Comprehensive Java assessment covering core Java, Spring Framework, microservices architecture, multithreading, and enterprise design patterns.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Coding Pro - Full Stack Development",
    test_type: ["Knowledge & Skills", "Simulation"],
    duration: 60,
    adaptive_support: "Yes",
    remote_support: "Yes",
    description: "End-to-end full-stack development assessment covering frontend (React/Angular), backend (Node.js/Python), REST APIs, databases, and system design.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Verbal Reasoning Test",
    test_type: ["Cognitive Ability"],
    duration: 19,
    adaptive_support: "Yes",
    remote_support: "Yes",
    description: "Measures the ability to understand, analyze, and draw logical conclusions from written passages. Essential for roles requiring strong communication and comprehension.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Numerical Reasoning Test",
    test_type: ["Cognitive Ability"],
    duration: 25,
    adaptive_support: "Yes",
    remote_support: "Yes",
    description: "Assesses ability to interpret numerical data, charts, graphs, and statistics for business decision-making. Ideal for analytical and finance roles.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Inductive Reasoning (Logical) Test",
    test_type: ["Cognitive Ability"],
    duration: 20,
    adaptive_support: "Yes",
    remote_support: "Yes",
    description: "Evaluates ability to identify patterns, logical rules, and trends in abstract data. Predicts capacity for problem-solving and strategic thinking.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "OPQ32 - Occupational Personality Questionnaire",
    test_type: ["Personality & Behavior"],
    duration: 45,
    adaptive_support: "No",
    remote_support: "Yes",
    description: "Comprehensive personality assessment measuring 32 workplace behavior dimensions including leadership style, interpersonal skills, and work preferences.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Motivation Questionnaire (MQ)",
    test_type: ["Personality & Behavior"],
    duration: 25,
    adaptive_support: "No",
    remote_support: "Yes",
    description: "Identifies key motivational drivers and energy sources in the workplace. Helps predict job satisfaction, engagement, and cultural fit.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Situational Judgement Test - Management",
    test_type: ["Simulation"],
    duration: 40,
    adaptive_support: "No",
    remote_support: "Yes",
    description: "Presents realistic workplace management scenarios to evaluate decision-making, conflict resolution, delegation, and interpersonal effectiveness.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Leadership Assessment Battery",
    test_type: ["Competency", "Personality & Behavior"],
    duration: 55,
    adaptive_support: "No",
    remote_support: "Yes",
    description: "Multi-dimensional leadership assessment evaluating strategic vision, team management, decision-making under pressure, and transformational leadership capabilities.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Communication Skills Assessment",
    test_type: ["Competency"],
    duration: 35,
    adaptive_support: "No",
    remote_support: "Yes",
    description: "Evaluates written and verbal communication competencies including clarity, persuasion, active listening, and cross-functional collaboration effectiveness.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Business Acumen Assessment",
    test_type: ["Competency"],
    duration: 30,
    adaptive_support: "No",
    remote_support: "Yes",
    description: "Evaluates understanding of business fundamentals, strategic thinking, financial literacy, market awareness, and commercial decision-making.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Graduate / Entry-Level Assessment Suite",
    test_type: ["Cognitive Ability", "Personality & Behavior"],
    duration: 50,
    adaptive_support: "Yes",
    remote_support: "Yes",
    description: "Comprehensive assessment battery designed for campus recruiting and graduate programs, combining cognitive ability, personality, and motivation measures.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Customer Service Assessment",
    test_type: ["Competency", "Simulation"],
    duration: 30,
    adaptive_support: "No",
    remote_support: "Yes",
    description: "Assesses customer-facing competencies including empathy, problem resolution, service orientation, and ability to handle difficult customer interactions.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Sales Assessment Battery",
    test_type: ["Competency", "Personality & Behavior"],
    duration: 45,
    adaptive_support: "No",
    remote_support: "Yes",
    description: "Comprehensive sales aptitude assessment covering prospecting skills, negotiation, relationship building, resilience, and target-driven motivation.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Mechanical Comprehension Test",
    test_type: ["Knowledge & Skills"],
    duration: 20,
    adaptive_support: "Yes",
    remote_support: "Yes",
    description: "Assesses understanding of basic mechanical and physical principles including forces, pulleys, gears, and electrical circuits for technical and engineering roles.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Checking & Attention to Detail Test",
    test_type: ["Cognitive Ability"],
    duration: 15,
    adaptive_support: "No",
    remote_support: "Yes",
    description: "Measures speed and accuracy in comparing and checking information. Critical for roles requiring precision in data entry, accounting, and quality assurance.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Teamwork & Collaboration Assessment",
    test_type: ["Competency"],
    duration: 25,
    adaptive_support: "No",
    remote_support: "Yes",
    description: "Evaluates collaboration competencies including conflict management, consensus building, cross-functional teamwork, and virtual collaboration skills.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Data Science & Analytics Assessment",
    test_type: ["Knowledge & Skills"],
    duration: 45,
    adaptive_support: "Yes",
    remote_support: "Yes",
    description: "Evaluates data science skills including statistical analysis, machine learning concepts, data visualization, A/B testing, and Python/R programming for analytics.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Agile & DevOps Assessment",
    test_type: ["Knowledge & Skills"],
    duration: 30,
    adaptive_support: "No",
    remote_support: "Yes",
    description: "Assesses knowledge of Agile methodologies, Scrum, Kanban, CI/CD pipelines, containerization, cloud infrastructure, and DevOps best practices.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Emotional Intelligence Assessment",
    test_type: ["Personality & Behavior", "Competency"],
    duration: 30,
    adaptive_support: "No",
    remote_support: "Yes",
    description: "Measures emotional intelligence dimensions including self-awareness, self-regulation, empathy, social skills, and emotional resilience in workplace contexts.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Critical Thinking Assessment",
    test_type: ["Cognitive Ability"],
    duration: 30,
    adaptive_support: "Yes",
    remote_support: "Yes",
    description: "Evaluates the ability to analyze arguments, evaluate evidence, identify logical fallacies, and make well-reasoned decisions under ambiguity.",
    url: "https://www.shl.com/solutions/products/assessments/"
  },
  {
    name: "Project Management Assessment",
    test_type: ["Competency", "Knowledge & Skills"],
    duration: 40,
    adaptive_support: "No",
    remote_support: "Yes",
    description: "Assesses project management competencies including planning, risk management, stakeholder communication, resource allocation, and agile/waterfall methodologies.",
    url: "https://www.shl.com/solutions/products/assessments/"
  }
];

export const LUCKY_QUERIES = [
  "Chief Technology Officer leading digital transformation for a Fortune 500 company",
  "Senior Machine Learning Engineer specializing in NLP and large language models",
  "VP of Engineering managing globally distributed teams of 200+ developers",
  "Head of Product for a high-growth SaaS startup disrupting the HR tech space",
  "Director of Data Science building predictive analytics platforms",
  "Principal Software Architect designing cloud-native microservices at scale",
  "Global Head of Talent Acquisition for a multinational consulting firm",
  "Senior Full-Stack Developer for a fintech company processing millions of transactions",
];

export function searchAssessments(query: string): Assessment[] {
  const lower = query.toLowerCase();
  const tokens = lower.split(/[\s,;.]+/).filter(t => t.length > 2);

  const synonyms: Record<string, string[]> = {
    python: ['python', 'programming', 'coding', 'developer', 'software'],
    sql: ['sql', 'database', 'data', 'query', 'queries'],
    javascript: ['javascript', 'js', 'frontend', 'front-end', 'react', 'angular', 'vue', 'web'],
    java: ['java', 'enterprise', 'spring', 'backend', 'microservices'],
    leadership: ['leadership', 'leader', 'manager', 'management', 'executive', 'director', 'vp', 'head', 'chief', 'cto', 'ceo', 'cfo'],
    communication: ['communication', 'writing', 'verbal', 'presentation', 'interpersonal'],
    sales: ['sales', 'selling', 'revenue', 'business development', 'account'],
    customer: ['customer', 'service', 'support', 'client', 'helpdesk'],
    data: ['data', 'analytics', 'analysis', 'statistics', 'machine learning', 'ml', 'ai', 'science'],
    cognitive: ['reasoning', 'cognitive', 'logical', 'analytical', 'problem-solving', 'critical thinking'],
    personality: ['personality', 'behavior', 'culture', 'fit', 'motivation'],
    teamwork: ['team', 'teamwork', 'collaboration', 'agile'],
    fullstack: ['fullstack', 'full-stack', 'full stack', 'frontend', 'backend'],
    mechanical: ['mechanical', 'engineering', 'technical', 'physical', 'electrical'],
    graduate: ['graduate', 'entry', 'junior', 'campus', 'intern', 'fresher'],
    project: ['project', 'management', 'pmp', 'scrum', 'kanban'],
    devops: ['devops', 'ci/cd', 'cloud', 'docker', 'kubernetes', 'infrastructure'],
    emotional: ['emotional', 'intelligence', 'empathy', 'eq'],
  };

  const scored = MOCK_ASSESSMENTS.map(a => {
    const text = `${a.name} ${a.description} ${a.test_type.join(' ')}`.toLowerCase();
    let score = 0;

    tokens.forEach(token => {
      if (text.includes(token)) score += 3;
      Object.values(synonyms).forEach(group => {
        if (group.includes(token)) {
          group.forEach(syn => {
            if (text.includes(syn)) score += 1;
          });
        }
      });
    });

    return { assessment: a, score };
  });

  scored.sort((a, b) => b.score - a.score);
  const results = scored.filter(s => s.score > 0).map(s => s.assessment);
  return results.length > 0 ? results.slice(0, 10) : MOCK_ASSESSMENTS.slice(0, 6);
}
