from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
course=json.loads((root/'data.json').read_text());essays=[]
def add(lecture,title,subtitle,body):
 sections=[]
 for chunk in body.strip().split('## ')[1:]:
  h,text=chunk.split('\n',1);sections.append({'id':f'section-{len(sections)+1}','heading':h,'paragraphs':[p.strip().replace('\n',' ') for p in text.strip().split('\n\n') if p.strip()]})
 n=sum(len(p.split()) for s in sections for p in s['paragraphs'])
 essays.append(dict(lecture=lecture,title=title,subtitle=subtitle,sections=sections,wordCount=n,readingMinutes=max(1,round(n/180)),sourceIds=next(c['sourceIds'] for c in course['concepts'] if c['lecture']==lecture)))
add(1,'Research foundations and ethical inquiry in SLP','From a clinical uncertainty to a transparent, useful and ethical investigation.', '''
## Research as systematic inquiry
Research is a planned investigation that uses explicit procedures to address uncertainty. In speech-language pathology, it may describe a communication pattern, assess a measurement tool, compare interventions or interpret service experiences. A clinician noticing that some families cannot attend appointments has identified a possible problem, but the observation is not yet a completed investigation. The researcher must specify what evidence is needed, how it will be obtained and what conclusions the design can support.

A research problem motivates inquiry; a research question states the uncertainty more precisely; objectives describe what the project intends to accomplish. Neither an objective nor a prediction guarantees a particular result. A defensible study can produce an unexpected or inconclusive finding while still contributing useful evidence, provided its procedures and limitations are reported honestly.

## Evidence-based practice and clinical relevance
Evidence-based practice integrates relevant research and individual clinical evidence with professional expertise and client or caregiver perspectives. A trial can inform treatment selection, but its group average does not settle every issue for an individual. The clinician must consider the match between participants, procedures, language background, resources and the client's priorities. Expertise helps make these judgments, while systematic outcome monitoring supplies evidence about the individual response.

Research can support theoretical understanding, assessment, prevention, service organization and outcome improvement. Questions about prevalence concern existing cases in a defined population and time frame. Incidence concerns new occurrence among people at risk over time. A school survey and a follow-up study can therefore answer different frequency questions even when they concern the same condition.

## Planning a coherent process
The research process connects question development, literature review, design, measurement, sampling, analysis and dissemination. These activities can be iterative: an initial search may reveal that a question is too broad or that an intended outcome cannot be measured appropriately. A protocol records the resulting plan, including eligibility, recruitment, procedures, outcomes and analysis. A timeline allocates realistic time for ethical review, recruitment and practical dependencies rather than assuming every stage begins immediately.

Feasibility includes access to participants, equipment, expertise, time and funding. SMART goals can help make tasks specific, measurable, achievable, relevant and time-bound, but they do not require every legitimate question to become a numerical endpoint. An experience-focused qualitative question may have a clear and feasible plan without treating meaning as a single scale score. Collaboration and supervision can strengthen the project, particularly when methodological or statistical expertise is required.

## Participant protection
Informed consent is a voluntary, understandable and continuing decision process. A signature alone does not establish comprehension or freedom from pressure. Information may need accessible wording, supported communication and an appropriate process for assessing decision-making capacity. Communication impairment should not automatically be equated with inability to consent. Research involving children may also require legally appropriate permission and meaningful assent where applicable, under the relevant review requirements.

Privacy concerns access to the person and their circumstances; confidentiality concerns protection of identifiable information. An interviewer may know a participant's identity while still maintaining confidentiality. Anonymity is a stronger and different claim. Removing names from a voice recording does not necessarily make the speaker unrecognizable. Access controls, secure storage, justified retention and careful reporting should match the data's actual sensitivity.

Beneficence requires minimizing avoidable harm and considering possible benefits. It does not permit promising improvement to every participant. Justice requires fair selection and a defensible distribution of burdens and benefits. Independent ethics review assesses the plan before relevant research activities begin, but approval does not end the researcher's responsibilities. New risks, changes or participant concerns still require attention.

## Evidence, statistics and interpretation
Descriptive statistics summarize observations. The mean is an arithmetic average, the median identifies the centre of ordered observations, and the mode is the most frequent value or category. Variability describes spread through quantities such as range and standard deviation. Groups with equal means can contain very different individual patterns, so summaries should be selected and interpreted carefully.

Statistical significance concerns a test result relative to a prespecified threshold under a model. A p value is not the probability that the null hypothesis is true and does not express the chance that every client will benefit. A frequentist confidence interval comes from a procedure with stated long-run coverage under assumptions; its width also communicates precision. Clinical importance requires additional judgment about magnitude, function, participation and client priorities. Association between two ratings also differs from agreement: consistently higher scores from one rater can coexist with high correlation.

## Reporting, collaboration and responsible use
A research report distinguishes background, procedures, observations and interpretation, often through an introduction-methods-results-discussion structure. Peer review can identify weaknesses and improve clarity, but publication is not a permanent certificate of correctness. Readers still need critical appraisal of relevance, sampling, measures, analysis and limitations.

Dissemination includes reporting unfavourable, null and uncertain results rather than circulating only positive findings. Grant proposals need a justified plan and budget, while collaboration requires agreed roles and responsible handling of data and credit. New technologies can generate useful research questions, but novelty does not itself establish effectiveness. The central principle is coherence: important questions should be investigated with feasible, ethical procedures and conclusions proportionate to the evidence.
''')
add(2,'Research approaches and designs','Choosing a strategy that matches the question and the inference required.', '''
## Approach, design and method
A research approach provides a broad orientation, a design organizes the inquiry and methods are specific procedures for obtaining or analyzing evidence. Quantitative, qualitative and mixed approaches are useful broad labels. A randomized trial, ethnography or sequential mixed-methods project describes more specific design choices. An interview, rating procedure or statistical comparison is a method. These terms overlap in some textbooks, but confusing their levels can make a proposal unclear.

Quantitative inquiry uses numerical measurement to describe patterns or examine relationships. It does not always manipulate a treatment. Qualitative inquiry investigates meanings, experience and processes in context through systematic interpretation. It is not an absence of rigor merely because its evidence is not reduced to group means. Deductive reasoning develops expectations from propositions or theory, while induction builds accounts from observations. Actual projects can use both forms of reasoning at different stages.

## Integrating mixed evidence
Mixed-methods research intentionally connects quantitative and qualitative components. The value lies in their integration, not simply placing numbers and quotations in the same document. In a convergent design, components address related questions within a coordinated phase and are brought together. Agreement can reinforce an account, while disagreement may reveal different contexts, samples or measurements.

An explanatory sequential design begins with quantitative findings and uses later qualitative work to investigate their meaning. An exploratory sequential design begins with qualitative exploration that informs subsequent quantitative development or testing. Meta-inferences explain what the combined evidence contributes beyond separate result sections. The design should state where and why this connection occurs.

## Intervention designs and control
A randomized controlled trial assigns enrolled units to conditions through a random mechanism. Its comparison may involve usual care or an active treatment rather than no support. Random assignment balances characteristics in expectation, but small groups can still differ by chance. Allocation concealment prevents prediction of upcoming assignments during enrolment; blinding concerns knowledge of assignment after allocation. These protections address distinct risks and should not be treated as interchangeable.

Quasi-experimental research evaluates interventions without random allocation in the relevant comparison. Existing clinic groups may make such work practical, but selection differences remain potential explanations for the findings. Measuring baseline values does not automatically remove all confounding. Treatment fidelity establishes what was delivered, while attrition and missing follow-up information affect how the comparison should be interpreted.

## Small-sample and case-based inquiry
A single-case experimental design uses repeated observations and planned changes to support within-case inference. A baseline describes performance before intervention, and a multiple-baseline design staggers introduction across participants, settings or behaviours. Replication of a change pattern helps demonstrate control without requiring withdrawal in every case. A simple before-and-after account of one client does not automatically meet this experimental standard.

A case study provides an intensive investigation of a bounded person, group or setting. It can reveal complexities and generate hypotheses, but the descriptive value of a case does not itself establish causation. The important distinction is the logic of the design, not simply whether the sample contains one person or many.

## Observational comparisons and time
Survey research systematically gathers information about characteristics, experiences or practices. Its usefulness depends on sampling, question construction and response patterns rather than a universal minimum sample number. A cross-sectional study observes a defined window, which can describe differences across age groups without proving each individual's developmental path. A longitudinal study follows units over time, revealing change and temporal order while remaining vulnerable to confounding, measurement problems and dropout.

Retrospective investigation uses information about earlier events, often from records. Prospective investigation plans observation as events unfold. These labels concern timing rather than randomization. A cohort follows a defined group, while a case-control design selects groups through outcome status and investigates prior exposures. Correlational research examines association without assigning the focal predictor; the existence of association alone cannot establish direction or exclude common causes.

## Synthesis, validity and replicability
Meta-analysis combines compatible effect estimates statistically. A collection of papers is not automatically a meta-analysis, and pooling does not repair biased or incompatible primary evidence. The synthesis method should address a defined question and report limitations, including uncertainty and variation across studies.

Internal validity concerns the credibility of conclusions within the study, particularly alternative explanations for an effect. External validity concerns application to relevant people and circumstances beyond it. Neither a natural clinical setting nor a controlled laboratory guarantees every form of validity. Replication can examine robustness and boundary conditions, so asking a similar question again can be scientifically justified. The best design is the one whose evidence and assumptions genuinely address the intended question, not simply the design with the most impressive label.
''')
add(3,'Definitions, variables and measurement','Turning meaningful constructs into interpretable observations.', '''
## Concepts and operational definitions
A variable can take different values across people, situations or occasions. It need not be manipulated: age, language history, response time and interview categories can all vary. A construct is a meaningful idea, such as participation or working memory, represented through selected indicators. A conceptual definition explains what the construct means; an operational definition specifies how the study observes, scores or manipulates it.

For intelligibility, an operational definition might state the speech task, listener characteristics, sampling procedure and percentage of words correctly transcribed. Saying that a child's speech is good is insufficient for replication. No single procedure necessarily captures every dimension of a broad construct, so measurement choices should be justified in relation to the question and intended interpretation.

## Roles within a research model
An independent variable is an assigned or explanatory factor examined in relation to an outcome. The dependent variable is the response being analyzed. In an experiment, therapy intensity may be assigned and speech accuracy measured. In observational work, a predictor may not have been manipulated at all. Calling it independent does not establish a causal effect. The same observed characteristic can occupy different roles in different questions.

A mediator represents a proposed pathway through which an effect occurs. Caregiver practice might be hypothesized to connect coaching with child outcomes. Mediators can be measured through suitable observations or indicators; they are not inherently invisible. A moderator concerns whether the relationship differs across levels of another variable, often expressed as interaction. Age-related variation in treatment effect is therefore a moderation question, not automatically evidence of mediation.

Controlled variables are held constant or addressed by specified procedures. A covariate is a variable included in an analytical model. A confounder provides an alternative explanation through relevant relationships with predictor and outcome. These terms should not become a justification for indiscriminately controlling every available variable. Adjusting for a variable on the treatment pathway or one selected through the wrong causal logic can distort the target comparison.

## Measurement scales and data forms
Nominal categories identify groups without inherent quantitative order. Coding diagnoses as 1, 2 and 3 does not make their mean a meaningful disease quantity. Ordinal scales establish order without demonstrating equal distances: mild, moderate and severe need not be equally spaced. Interval scales support meaningful equal differences but lack a meaningful absolute zero, as illustrated by Celsius temperature. Ratio scales additionally support ratios, as with comparable durations measured in milliseconds.

The arithmetic belongs to the measurement interpretation, not merely to printed numbers. Standardized test scores should not automatically be assumed to prove equal intervals in underlying ability. Decibels require special care because they express logarithmic ratios to a reference; zero decibels is not necessarily physical silence. Underlying intensity and its dB expression therefore do not share identical arithmetic properties.

Discrete variables take separate countable values, such as error counts. Continuous quantities, such as duration, vary conceptually over a continuum even when recordings are rounded. Coding, recording precision and underlying measurement type are related but distinct considerations.

## Quality, error and change
Reliability concerns consistency or precision under defined conditions. Inter-rater evidence examines how raters score the same material, while test-retest evidence concerns stability when the target is expected to remain stable. A genuine therapeutic change should not automatically be treated as failure of test-retest reliability. Measurement error must be considered relative to the size and intended use of a score difference.

Validity concerns support for the interpretation and use of scores. A tool supported for one population or purpose is not automatically suitable for every language group or decision. Responsiveness concerns detection of relevant change. Diagnostic classification and short-term outcome measurement may require different instrument properties. A reliable, useful diagnostic test can still be insensitive to small gains over a brief treatment interval.

## Domains measured in SLP
Demographic information includes age, education and language history, but these descriptors should not be used as deterministic explanations of individual ability. Speech measures can concern articulation, fluency, voice and prosody. Language outcomes can concern vocabulary, syntax, comprehension, pragmatics and narrative organization. A single vocabulary score does not summarize every aspect of communication.

Phonological-processing tasks examine sound-based information, such as deleting a phoneme. Working memory involves maintaining and manipulating information, processing speed concerns response or processing rate, and executive functions include regulation, inhibition and shifting. These cognitive demands may influence language tasks without being identical to language ability. Sensory access and processing also require attention: normal peripheral hearing does not settle every question about complex auditory task performance.

## Culture, development and intervention response
Assessment should consider linguistic structure, experience and cultural communication norms. A difference from English conventions is not by itself a disorder. Developmental age ranges describe broad patterns rather than exact deadlines for every child. Relevant comorbidities can influence measurement or participation, but a diagnosis should not be taken to imply one universal profile.

Acquisition, generalization and maintenance describe different intervention outcomes. Acquisition concerns initial learning of trained targets. Generalization concerns untrained items, situations or partners. Maintenance concerns persistence after an appropriate interval. Measuring one does not establish the others. Missing observations further complicate interpretation when participants do not complete planned assessments. A sound study therefore defines its constructs, procedures, measurement quality and follow-up carefully before treating score changes as meaningful evidence.
''')
add(4,'Sampling: selecting participants and judging scope','Probability, practical recruitment and the limits of generalization.', '''
## Population, frame and sample
Sampling connects the group a question concerns with the people or units actually observed. The target population defines intended scope; the accessible population is reachable through practical recruitment arrangements. A sample contains selected or participating units. A sampling frame is the list or structure used for selection. School lists, for example, can omit eligible children or contain outdated entries, affecting coverage even before anyone is randomly selected.

A census attempts to include every member of a defined population. Merely inviting everyone does not establish complete observation if some decline or cannot be contacted. Inclusion criteria define eligibility, while exclusion criteria specify justified reasons for omitting otherwise relevant individuals. These rules should align with the question and be applied consistently rather than adjusted secretly to obtain a preferred result.

## Probability selection
Probability sampling uses a chance mechanism with known nonzero inclusion probabilities. Equal chances characterize familiar simple random sampling but are not required by every probability design. In the standard fixed-size simple random sample, every possible subset of that size is equally likely. A random generator selecting unique IDs from a complete list is different from recruiting whoever volunteers first.

Systematic sampling selects at intervals after an appropriate random start. In a simple example, 300 listed people and a desired sample of 15 give an interval of 20. Frame ordering matters: a repeating pattern aligned with that interval can distort the selection. A procedure needs more than the phrase every twentieth person to establish that it has the intended properties.

## Strata, allocation and clusters
Stratified random sampling partitions the population into relevant subgroups and randomly samples within each. Proportional allocation preserves their population shares in planned sample counts. If four academic years contain 80, 60, 40 and 20 students, a proportional sample of 50 allocates 20, 15, 10 and 5. Disproportionate sampling may deliberately oversample a small subgroup, with design-aware analysis and appropriate weighting where needed.

Cluster sampling instead selects groups, such as schools, and observes eligible units within selected groups. A one-stage design includes all eligible children in selected schools; a multistage design samples children again within them. Strata are represented through within-stratum selection, while ordinary cluster sampling selects some groups rather than every group. Calling a cluster a mini-population is only an analogy: real schools need not perfectly reproduce district composition, and children within schools may be statistically related.

## Nonprobability recruitment
Convenience sampling prioritizes accessibility. Purposive sampling deliberately selects information-rich cases relevant to the question, often useful for detailed qualitative inquiry. Neither method is automatically invalid, but neither gains known selection probabilities merely through diversity or researcher expertise. The reasoning for selection and the scope of conclusions must be explicit.

Consecutive sampling includes every eligible accessible case in a defined stream over a specified period or until a stated endpoint. It does not mean selecting arbitrary groups one after another after analyzing each. Quota sampling sets subgroup counts and recruits until these are filled without necessarily randomizing selection within them. Equal numbers of boys and girls therefore establish quotas, not automatically stratified random sampling.

Snowball sampling recruits through participant referrals and can help identify hard-to-reach groups. Networks, initial contacts and willingness to refer can strongly shape the resulting sample. Privacy and voluntariness require attention, especially when acquaintances supply information about potentially eligible people.

## Bias, chance and sample size
Sampling error is random variation across repeated samples, whereas sampling bias is systematic distortion. Nonresponse bias arises when the likelihood of responding relates to factors important to the inquiry. Increasing a sample from one restrictive clinic can reduce random error while leaving selection bias intact. A larger biased sample may simply estimate the wrong target more precisely.

Random sampling selects units from a population. Random assignment allocates enrolled units to conditions. A study can recruit conveniently and then randomize treatment, improving the internal comparison without making the sample representative of all potential clients. The distinction is fundamental when interpreting a trial's applicability.

Sample-size planning should consider the question, expected variability, target effect or precision, design, clustering, attrition and practical constraints. There is no universal rule that thirty participants make every project adequate. Clear reporting of eligibility, approaches, refusals, enrolment and analyzed observations allows readers to judge selection and scope. Good sampling is a coherent and transparent strategy, not simply a large final number.
''')
add(5,'Developing strong research questions','Connecting clinical observation, evidence gaps, outcomes and feasible inquiry.', '''
## From interest to uncertainty
A broad interest identifies an area, but a research question states what remains uncertain and what evidence could resolve it. An SLP may notice variation in attendance across service formats. Before concluding that one format is better, the researcher should review existing evidence, consider alternative explanations and identify the particular outcome of interest. An objective then describes the intended investigation without guaranteeing its result.

Topic refinement narrows the population, concept, setting, comparison or interval as appropriate. The aim is not to make the title sound complicated, but to create an inquiry that can be answered. A research gap must be supported by a relevant search and appraisal. Personal unfamiliarity with a topic does not establish that nobody has studied it, and justified replication can be valuable even when earlier work exists.

## Different questions need different evidence
Descriptive questions examine characteristics, frequency or distribution. Association questions examine relationships among measured variables. Causal questions ask about effects attributable to an intervention or exposure, requiring design and assumptions appropriate to that attribution. Experience questions seek meaning and perspectives in context. None of these forms becomes superior simply because it sounds more technical.

For example, asking how adults who stutter describe workplace participation naturally supports contextualized qualitative evidence. Asking whether assignment to one service changes an outcome calls for a defensible effect comparison. An uncontrolled interview study cannot estimate population incidence merely because many participants discuss a shared experience. Conversely, a numerical mean difference does not by itself explain the meaning people give to a service.

## Specifying a treatment question
A focused intervention inquiry should identify the relevant population, intervention, comparator and outcome, often with a clear time element. Population characteristics may include age, diagnosis and language background where necessary. An intervention should be described through actual delivery, procedures and dosage rather than a label alone. Usual care, an active alternative and no treatment answer different questions and raise different ethical considerations.

The outcome must reflect the intended construct. Everyday communication participation, target-sound accuracy and a structural anatomical measure are not interchangeable. In particular, the provided coaching example should not imply that behavioural practice automatically corrects structural velopharyngeal dysfunction. A study should measure what the intervention plausibly targets and avoid turning a convenient test score into an unsupported claim about another construct.

## Alignment with design and analysis
Question-design alignment means selecting a strategy whose evidence can address the inquiry. Question-measure alignment means that observations support the intended interpretation. Question-sample alignment means recruiting people or cases relevant to the question, rather than relying on a large unrelated group. These relationships form one chain: a clear question cannot compensate for an incompatible outcome or sample.

Directional hypotheses predict a direction, while null hypotheses provide specified reference claims for tests. Predictions should be justified, and results must remain open to contradiction. A prespecified primary outcome anchors the main inference and often sample-size planning. Secondary outcomes answer supplementary questions, with appropriate attention to uncertainty and multiple comparisons. Choosing the smallest p value after testing many outcomes and calling it primary is a selective-reporting problem.

## Feasibility, ethics and scope
A researchable question must fit available participants, skills, time and resources. Rare populations may require multisite collaboration, repeated-observation designs or a more modest scope. These constraints should lead to honest adaptation, not invented observations or hidden changes in criteria. Qualitative work can use purposive information-rich cases without pretending to estimate population proportions.

Ethical answerability is equally important. The scientific value of a question does not justify coercion or an unjustified denial of appropriate care. Clear consent arrangements, suitable comparisons and a proportionate burden belong in the plan. Sample-size expectations should also match the proposed effect or precision; under otherwise fixed conditions, smaller target effects usually require more information.

## Refining before collecting
A practical refinement process moves between observation, literature, question components and feasible methods. Peer or supervisor feedback can expose ambiguity before data are collected. Ask whether each planned observation answers a stated part of the inquiry and whether the intended conclusion would exceed what the design supports. A strong question gives a project direction while leaving its answer genuinely open to evidence.
''')
add(6,'Frameworks for research questions in SLP','Using PICO, PEO, PCC, SPIDER, SPICE and ECLIPSE accurately.', '''
## Frameworks as organizing aids
A research-question framework separates an inquiry into useful components. It helps identify what is being studied, but does not establish that the design is valid or that an expected result will occur. Mnemonics are selected for fit rather than imposed as universal rules. The same initial letter can mean different things in different frameworks, so memorizing a word without its role can produce incorrect mappings.

These tools also differ from search strings. A well-specified question may contain more detail than should be joined with AND in the initial database search. Comparators and outcomes can be inconsistently mentioned or indexed. Searching every possible component can therefore miss relevant records even when the question itself is excellent.

## PICO and PICOT
PICO identifies Population, Intervention, Comparison and Outcome. In a question about ultrasound biofeedback for a specified child group, the population defines the people, biofeedback defines the intervention, an alternative therapy defines the comparison and a specified accuracy measure defines the outcome. PICOT adds Time, such as outcomes after ten weeks. Time clarifies the intended interval but does not establish that allocation is random.

The population should be sufficiently characterized without arbitrary restrictions. The intervention needs actual procedural detail, and the comparison should be clinically relevant and ethically defensible. An outcome requires a construct and interpretable measurement, not simply the hope of improvement. PICO is well suited to comparative intervention questions, but it is not a substitute for protocol-level design or evidence about measurement quality.

## PEO and PECO
PEO identifies Population, Exposure and Outcome. PECO adds a Comparator, and time can also be specified where needed. Exposure may be naturally occurring rather than assigned. A study relating documented screen-time exposure to a vocabulary measure therefore differs from assigning a therapy. A screening programme that is deliberately introduced should not automatically be classified as an unassigned risk exposure merely because the example appears under an exposure mnemonic.

Exposure-based questions still require attention to timing, measurement and confounding. The framework names the components but cannot turn a cross-sectional association into a demonstrated causal pathway. The comparison can be a different exposure level or category when justified by the question.

## PCC for evidence mapping
PCC identifies Population, Concept and Context, commonly used to frame a scoping review. Adults with aphasia can be the population, telepractice the concept and home or community services in a stated region the context. The concept can be a measure, phenomenon or service rather than an assigned intervention. Context can include geographical, institutional or sociocultural conditions.

A scoping question commonly asks what evidence exists, how a topic has been studied and where gaps remain. It does not necessarily estimate one treatment's superiority. The two C components must therefore remain concept and context rather than being mistaken for two comparison groups.

## SPIDER for experience-oriented inquiry
SPIDER identifies Sample, Phenomenon of Interest, Design, Evaluation and Research type. In a caregiver study, the sample might be parents with relevant experience, the phenomenon access to services, the design semi-structured interviews, the evaluation their perceptions and the research type qualitative. The mnemonic was developed to support qualitative evidence synthesis and can inform related mixed-methods questions.

Phenomenon of interest and evaluation are connected but distinct: one identifies the experience or process and the other the views or material examined. A procedure such as an interview may appear under design in the mnemonic, but a full proposal should still distinguish a collection technique from its broader methodology. The framework does not make a statistical outcome compulsory for an experience question.

## SPICE for service evaluation
SPICE identifies Setting, Perspective, Intervention or Interest, Comparison and Evaluation. The earlier handout's inconsistent labels need correction. An outpatient clinic is setting; adults using the service provide a perspective; group therapy can be the intervention; individual therapy the comparison; and communication confidence the evaluation criterion.

This arrangement broadens a service question beyond a narrow treatment label. Perspective highlights whose judgment or experience matters, while setting identifies where the service occurs. An evaluation can include benefit, satisfaction or other relevant criteria. These elements should not be swapped simply because a different framework uses S for sample or P for population.

## ECLIPSE and choosing a fit
ECLIPSE identifies Expectation, Client group, Location, Impact, Professionals and Service. In a pathway-improvement inquiry, expectation is the improvement or information sought, client group identifies users, location identifies delivery context, impact states the intended difference, professionals identify staff and service names what is being investigated. SE stands for Service here, not standard error.

The choice depends on purpose: intervention comparison, exposure relationship, evidence mapping, experience or service management. A sensible framework makes assumptions and boundaries visible while leaving design, recruitment, measurement and analysis to be justified. Its value is clarity, not the appearance of having completed methodology by selecting an acronym.
''')
add(7,'Finding and organizing the research literature','Building a transparent search that supports critical synthesis.', '''
## Why review the literature
A literature review critically organizes what is known, disputed and insufficiently investigated. It provides context, justifies a question and informs design, measurement and feasibility. A list of article summaries is only an intermediate product. The final account should connect findings across studies, consider their limitations and explain how the evidence bears on the current inquiry.

Searching supplies material for that synthesis. A keyword can be useful without retrieving every relevant record. Terminology changes across authors, disciplines and time, so a defensible strategy considers alternative expressions and suitable indexing terms. Search synonyms expand retrieval, but this does not make clinically distinct conditions conceptually identical.

## Building concept blocks
A concept block groups alternative expressions for one idea. OR ordinarily retrieves either or both alternatives, broadening coverage within that block. AND joins different concepts and typically narrows retrieval relative to either alone. Parentheses clarify intended combinations, such as Population AND (term A OR term B). Database-specific precedence and syntax should be checked rather than assumed.

NOT removes records meeting an exclusion. It needs caution because a relevant study containing both an eligible and an excluded population can be lost. Phrase searches and truncation can also be useful, but their behaviour varies by platform. A stem-and-wildcard example should be tested in the actual database. Search mechanics are operational decisions, not universal formulas detached from the interface being used.

## Free text and controlled vocabulary
Controlled vocabulary provides standardized concept labels. MeSH is the NLM vocabulary used for MEDLINE indexing, organized through relationships that can include broader and narrower headings. The tree structure helps identify whether a heading or its narrower terms match the question. Free-text searching uses terms in specified fields and can retrieve recent or otherwise incompletely indexed records.

PubMed includes MEDLINE and other bibliographic records, but not every citation has complete MeSH indexing or free full text. Title-abstract tags define where terms are matched; they do not search the entire publisher article. A balanced strategy often combines appropriate headings and text terms, while checking the consequences of field restrictions and automatic mapping.

## Selecting complementary resources
Database choice should reflect the disciplinary scope of the question. Biomedical resources can be supplemented by allied-health, psychology or education databases, such as CINAHL, PsycINFO and ERIC. ASHA publications provide communication-sciences coverage, while citation indexes can support forward discovery. These resources overlap but do not contain identical records, so one publisher platform should not automatically be treated as a worldwide search.

Backward citation searching examines sources cited by a known article; forward searching identifies later work citing it. Google Scholar can support broad discovery and citation links, but changing ranking and coverage complicate complete reproducibility. It should complement a carefully documented strategy rather than be presented as a guarantee of exhaustive retrieval.

## Reproducibility and search performance
A search log records source, date, exact query, limits and retrieval count. A statement that several databases were searched is insufficient to reproduce what happened. Searches must be translated to each database's headings and field syntax rather than copied mechanically. Language, date and publication-type restrictions need justification because they can remove relevant evidence.

Sensitivity concerns retrieving relevant material; precision concerns how much of the retrieved material is relevant. A narrow search can look precise while missing important studies. Testing against known relevant papers and reviewing unexpected exclusions can improve the strategy. No tidy search string by itself proves complete coverage of an evolving literature.

## Organizing evidence and writing ethically
Reference managers such as Zotero, EndNote and Mendeley can organize records and support citations, but imported metadata still require checking. Consistent file names, folders, tags and backups help maintain a usable collection. Deduplication should merge repeated records of the same report without deleting distinct studies merely because they discuss similar topics.

An evidence matrix gives each study a row and uses comparable columns for question, design, sample, outcomes, findings and limitations. Reading across studies helps move from summary to synthesis. Paraphrasing requires original expression that preserves meaning and retains attribution. A low similarity score cannot prove ethical use of ideas, and a citation alone does not authorize copying an unmarked passage. Searching, organizing, appraising and attributing evidence are connected responsibilities, not separate mechanical chores.
''')
add(8,'Critical reviewing, synthesis and responsible referencing','Turning selected studies into a balanced argument.', '''
## Choosing the review purpose
Narrative, systematic and scoping reviews serve related but different purposes. A narrative overview can develop background or theory, but should explain its scope and reasoning fairly. A systematic review uses explicit planned methods to answer a defined question. It may produce a narrative synthesis when pooling is inappropriate. Meta-analysis is a statistical technique, not a compulsory ingredient that determines whether a review is systematic.

A scoping review maps evidence types, concepts and gaps around a broader question, commonly organized with PCC. It still uses systematic methods of identification and selection. Critical appraisal is not mandatory for every scoping purpose, but it is not forbidden. The choice should reflect the review's aims, and an appraisal decision should be explained rather than made through an absolute rule.

## Protocols and transparent selection
A review protocol records intended eligibility, sources, selection, extraction and synthesis procedures. Appropriate registration or public posting makes plans visible and helps distinguish planned from selective decisions. Registries have different scopes and requirements; a particular registry is not automatically suitable for every review. Amendments can be necessary, but should be described and justified.

Deduplication manages repeated retrievals of a report. Title-abstract screening identifies potentially eligible records, and full-text assessment resolves eligibility and supports extraction. Independent assessment and a defined disagreement process can reduce selection errors. Reporting should distinguish records, reports and studies: a study may produce several publications, and one publication may appear in several search exports.

## Reporting versus quality
PRISMA 2020 supports reporting of systematic reviews through checklists and flow information. PRISMA-ScR addresses scoping reviews. These are reporting tools rather than guarantees of good conduct or substitutes for risk-of-bias assessment. SANRA offers a structured approach to aspects of narrative review assessment. A recognizable checklist name should therefore be matched to its actual purpose.

Risk-of-bias appraisal considers how methods may systematically distort a result. RoB 2 addresses randomized trial results, while ROBINS-I resources address nonrandomized intervention studies. AMSTAR 2 appraises healthcare intervention reviews. CASP and JBI provide design-specific resources. Using a tool requires its appropriate version and guidance; it is not enough to attach the acronym to an arbitrary numeric quality score.

## Appraising and extracting evidence
Appraisal examines recruitment, allocation, confounding, measurement, missing data and interpretation as relevant to the design. Sample size should be justified in relation to the question, and measures should fit the target population and intended use. A statistically significant outcome need not be meaningful for everyday participation. Applicability to Urdu- or Punjabi-speaking clients requires attention to language, context and procedures rather than an assumption that all clinical settings are equivalent.

Data extraction records comparable fields such as population, design, intervention, comparator, outcome, estimate and limitation. Scoping data charting may emphasize settings, concepts and evidence forms rather than one pooled effect. Extraction should include contradictory and unfavourable findings, not only results supporting the reviewer's position. Important fields should be checked against the original source.

## Building a synthesis argument
Thematic synthesis groups evidence around substantive ideas. Methodological comparison asks whether differences in design, measurement, participants or follow-up help explain disagreement. A strong paragraph can establish an area of agreement, qualify its evidential strength, contrast a relevant finding and identify a justified uncertainty. The point is not to force every paragraph into a repetitive template, but to make reasoning across sources explicit.

An evidence hierarchy can orient intervention questions, but design rank alone is insufficient. A biased review does not become reliable because it sits high on a diagram, and qualitative evidence may be particularly appropriate to experience questions. Citation patterns should support the actual claims rather than use a long reference list as a substitute for evaluation.

## Referencing and automated assistance
Vancouver commonly assigns numbers in order of first citation and reuses a source's number when it is cited again. The reference list follows that numerical sequence. Author limits, punctuation and journal abbreviations depend on the required variant, so a teaching rule about six authors should not be treated as an exceptionless requirement of every biomedical journal. NLM Citing Medicine and the target journal's instructions support checking.

Zotero can import records, organize collections, merge duplicates and link citations to a generated bibliography. Imported author names, titles, identifiers and journal details still require review. Citation existence and claim support are separate checks: an authentic DOI does not prove that an accompanying summary accurately states the findings.

AI tools may assist discovery, mapping, screening prioritization or wording, but can invent references, misdescribe studies or miss evidence outside their indexes. Humans remain responsible for source verification, appropriate disclosure and compliance with relevant authorship and data policies. Identifiable participant material should not be uploaded to an unapproved service. Responsible reviewing therefore combines transparent procedures, balanced synthesis and accountable use of both bibliographic and automated tools.
''')
add(9,'Measuring change: aligning questions, design and analysis','A critical explanation of the actual tutorial supplied as PDF Research Question.pdf.', '''
## Identifying the supplied reading
The file named PDF Research Question.pdf is Melissa J. Skoczylas's 2019 tutorial, Congruence in Research Question, Design, and Analysis: A Tutorial on the Measurement of Change in Clinical Speech and Language Research. It uses a hypothetical clinical scenario and artificial example data to explain decisions about evaluating change. The teaching values illustrate procedures; they are not observations proving that a real programme is effective.

Its central contribution is congruence. A question about greater change, a question about final scores and a question about everyday participation do not necessarily require the same outcome or analysis. The researcher should first state the target comparison, then select a design and method capable of addressing it. Software availability cannot resolve a mismatch between those components.

## Change scores and group comparisons
Under a posttest-minus-pretest convention, an individual scoring 12 before and 18 after has a gain of 6. With the same complete participants, a group's mean gain equals its posttest mean minus its pretest mean. Comparing mean gains between groups asks whether observed average change differs, whereas comparing final means asks about final values. The interpretation also depends on direction: an increase in errors is not improvement merely because the gain is positive.

The distinction between within-person calculation and between-group analysis is important. Each gain uses two observations from one participant, but gains from two different groups are not thereby paired across groups. A paired analysis addresses linked observations; an independent-groups comparison addresses different participants. Statistical dependence, clustering and matching must reflect the actual study rather than an assumption that every pre-post problem uses one automatic test.

## Nonequivalent groups and alternative explanations
Clinical groups may be predetermined by service arrangements or participant choices. Such nonequivalent-group designs can be practical but remain vulnerable to selection differences. A baseline assessment reveals some differences without proving the groups are equivalent. Subtracting baseline also does not guarantee removal of unmeasured confounding or different developmental trajectories.

Maturation concerns natural development over time, history concerns other events during the study and instrumentation concerns changes in assessment procedures. A fan-spread pattern can occur when groups already differ in their rate of growth. Additional pretreatment observations can reveal trends that two endpoints conceal. Regression to the mean can make unusually extreme noisy initial scores less extreme on repetition; movement toward average alone is not proof of treatment benefit.

## Choosing a responsive measure
Floor effects compress observations near a lower limit, while ceiling effects restrict the observable upper range. A task that places most participants at maximum before treatment cannot capture much further measured improvement. That does not establish that no further functional change is possible. Outcome instruments must be relevant, interpretable, reliable and responsive over the intended interval.

Diagnostic tools and criterion-referenced probes serve different purposes. A probe closely matching the target can be useful, but clinician creation alone does not demonstrate measurement quality. Repeated observations should use comparable constructs and units. A five-point change is hard to interpret if scale meaning or task demands change substantially across the measurement range. Follow-up can examine maintenance and reveal patterns hidden by an immediate posttest.

## Power, assumptions and analytical choices
Power is the probability of rejecting a false null for a specified alternative under stated conditions. Type I error concerns rejecting a true null; Type II error concerns failing to reject a false one. Sample-size planning depends on target effect, variability, threshold, design and other assumptions. There is no universal number that makes every design adequately powered or unbiased.

The tutorial's rule-of-thumb language about thirty participants must not be taken to mean that raw observations become normal. Large-sample approximations concern relevant sampling distributions under conditions. Standard deviation describes spread among observations, while standard error concerns sampling uncertainty in an estimator. Neither should be inferred solely from how smooth a chart appears.

For independent groups, gain values can be compared using a suitable mean-comparison method. Welch's t test does not require the pooled equal-variance assumption. One-way ANOVA addresses means across a factor's groups, with specific contrasts requiring appropriate interpretation. A within-group change test does not by itself demonstrate a between-group treatment difference.

## Baseline adjustment and effect interpretation
Baseline-adjusted analysis models final outcomes conditional on baseline and other justified covariates. Gain comparisons and adjusted final-value comparisons can estimate different contrasts and rely on different assumptions. The provided tutorial's cautions should not be turned into a blanket ban on adjustment in nonrandomized studies or automatic trust in any randomized analysis. A clear estimand, measurement model and defensible causal assumptions remain necessary.

A standardized mean difference expresses a contrast relative to a stated standard deviation convention. Hedges g additionally incorporates a small-sample correction; it is not distinguished from Cohen d solely by the word pooled. Effect-size magnitude, statistical uncertainty and clinical importance are separate issues. A large standardized effect does not establish that every individual benefits or that a score change meets the client's priorities.

## Interpreting a complete pattern
Group averages can conceal heterogeneous individual responses. Functional participation outcomes can complement targeted language probes, and plots can reveal instability, outliers or compression. Sensitivity analyses examine whether conclusions depend on plausible analytical choices; they should not become a search for whichever model gives significance.

The main lesson is careful alignment rather than loyalty to one procedure. Define the question, observe suitable data, examine threats and assumptions, choose an analysis matching the target and state conclusions proportionate to the evidence. That reasoning connects the tutorial to the whole course: good clinical research depends on how its components work together.
''')
assert len(essays)==9
(root/'essays.json').write_text(json.dumps(essays,ensure_ascii=False,indent=2));(root/'essays.js').write_text('window.LECTURE_ESSAYS = '+json.dumps(essays,ensure_ascii=False,separators=(',',':'))+';\n')
print('Essays:',[(e['lecture'],e['wordCount']) for e in essays],'; total',sum(e['wordCount'] for e in essays))
