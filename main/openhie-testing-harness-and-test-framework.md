A Health Information Exchange (HIE) makes the sharing of health data
across information systems possible. Like a universal translator, an HIE
normalizes data and secures the transmission of health information
throughout databases, between facilities, and across regions or
countries.

## Background

The OpenHIE community has collaboratively developed a HIE architecture.
Several software applications have been identified as reference
applications that implement parts of the specification, and they work
together as components of the OpenHIE Architecture Specification. There
has been no empirical way to test the compliance of these technologies
to the architecture specification. This testing approach should evaluate
the ability of these tools to meet the

- Interoperability requirements
- Functional requirements and to a degree
- Non-functional requirements.

Digital Square, under its mandate to promote the development, adoption,
and reuse of global goods, and helps increase their availability,
adaptability, and maturity has contracted Argusoft India Ltd.
[1](https://argusoft.com/) to develop a harness and complete test
framework that will facilitate testing the conformance of technologies
to the OpenHIE Architecture specification and health and data content,
as specified by WHO SMART Guidelines.

The resulting solution will be leveraged by other software applications
and tools, and as such should have a permissive open-source license as
it may be leveraged by vendors developing OpenHIE/SMART Guidelines
compliant software and other teams, such as the WHO Digital Health
Clearinghouse and the local country validation laboratories to test
compliance of digital health solutions to WHO SMART Guidelines
compliance requirements and/or their defined requirements.

> **Testing Harness**
>
> Digital Square refers to a test harness as a collection of tools and
> data used to test an application for conformance to a defined
> specification. The test harness is envisaged to be comprised of the
> test execution engine, test scripts and data used in testing with a
> clear separation of concerns between components.  
> The testing harness will be comprised of test execution engines and
> test script repositories. A test execution engine is the software used
> to perform the test, not the software being tested. The test script
> repository is the location where test scripts and cases are stored.
> The results are to be collated and presented as a report.  
> Not to be confused with a test framework, a testing harness is the
> collection of software and test data used to test a digital health
> solution (software), whereas test frameworks are the set of processes
> and procedures through which tests are designed and implemented.

## Vision

The testing harness and test framework will use the Gherkin language to
describe the test features (cases). It will also at the minimum have the
test execution engine, the test scripts and test data (See draft
architecture diagram below). The overall technology stack to be used is
yet to be decided at this time, and the stack will be shared here after
it is agreed upon.

## Roadmap

The project is expected to run through the end of June 2024 according to
the timeline below.

<figure>
<img src="Testing-harness-time-line.PNG" title="Development timeline"
width="800" />
<figcaption>Development timeline</figcaption>
</figure>

## Documentation and Architecture

This is the architecture that is currently proposed. This architecture
is subject to change as the development progresses.

<figure>
<img src="Testing-harness-architecture.png"
title="Proposed architecture, subject to change." />
<figcaption>Proposed architecture, subject to change.</figcaption>
</figure>

The documentation will be developed and published on the web. Once
complete, the link to the published documentation will be shared here.

## Contributing

The development of the testing harness and test framework will be open
to the community. The Argusoft team will meet twice a month to provide
progress updates and to also get community feedback. The meetings will
take place at the OpenHIE DevOps calls
[2](https://wiki.ohie.org/display/CP/DevOps+Subcommunity+Calls), and on
the OpenHIE Architecture and Standards calls
[3](https://wiki.ohie.org/pages/viewpage.action?pageId=11370513). The
community and all other interested stakeholders are highly encouraged to
participate.

## Global Goods response to COVID-19

<a href="COVID-19" class="wikilink" title="Read more here">Read more
here</a> about the adaptions made by global goods to support COVID-19
response activities.
