---
title: Shelf Readiness
nav_order: 1
---

# Introduction

The term âshelf-ready,â and the broader concept of âshelf readiness,â
stem from the need to ensure that digital health global goods,
particularly software, are ready to be deployed as stand-alone products
which meet the primary data use needs of a tool. While not referring to
a monolithic approach the concept of stand-alone refers to the tools
being packaged and complete in the view of having available and
installed all required dependencies and functions to achieve the
intended feature sets. Shelf readiness aims to allow implementers and
decision makers to have a higher level of confidence in the solutions as
they would be well presented in their product information, ability to
perform desired functions as well as interoperability workflows /
metadata synchronizations and deployment aspects, to name a few areas.

Digital Square has framed three tiers of shelves around the scaffolding
of the OpenHIE architecture to describe conceptual groupings of tools
within the space; with the first set of shelves framed around the (i)
Business Domain Services, (ii) Metadata Management/Registry Services and
(iii) Point of Services.

Technologies and software that are shelf ready should strive to support
the Installation Qualification (IQ), Operational Qualification (OQ), and
Performance Qualification (PQ) of software validation, in both tool and
implementation, and through this allow themselves to showcase their
readiness for safe and effective use and function. Digital Square has
outlined the following framework in guidance of technologies that are
shelf ready. The framework flows around the following areas:

## Global Goods Maturity Model {#global_goods_maturity_model}

Shelf-ready software and tools show a high level of maturity across the
[global goods maturity
model](https://wiki.digitalsquare.io/index.php/What_are_Global_Goods#Maturity_Model).
While high scores across all dimensions are ideal, achieving the levels
indicated below are prioritized:

- Global Utility
  - Digital Health Interventions (High)
  - Source Code Accessibility (High)
- Community Support
  - Software Roadmap (medium)
  - User Documentation (medium)
  - Multi-lingual Support (medium)
- Software Maturity
  - Technical Documentation (medium)
  - Software Productization (medium)
  - Interoperability & Data Accessibility (medium)
  - Security (medium)
  - Scalability (medium)

Further refinement of this model would see that software and tools
exhibit strong features and functionality in the areas of:

### Installation and Deployment {#installation_and_deployment}

Tools and technologies should not only follow international conventions
to support industry and enterprise installation and deployment patterns
but strive to support the [Instant
OpenHIE](https://wiki.ohie.org/display/resources/Instant+OpenHIE)
deployment and configuration requirements to form part of the large
infrastructure. This is inclusive of:

- Harmonized containerization approaches with the Instant OpenHIE
  project.
- Development of synchronization tools (e.g., OpenHIM mediators) between
  the software tool and metadata registries (facility, client,
  terminology) using appropriate IHE profiles of HL7 FHIR.
- Scripted configurations and data sets (as required) to showcase the
  functionality of base use cases.
- Existing documentation that allows implementers to validate that the
  initial installation of the tool is as per expected to support IQ.
  Functionalities and artifacts could include documented âexpectedâ
  state of successful installation, installation reports validating all
  services are operational, initial system check tests to support
  successful and correct installation, etc.

### Quality Assurance and Testing {#quality_assurance_and_testing}

Strong and empirical evidence of well-thought-out quality assurance
patterns to validate functionality and provide a sustained and
consistent base of evidence that the software both meets the functional
requirements or feature sets but also is built as expected. Shelf-ready
tools should strive towards having a documented testing strategy that
covers any major risk areas and business critical functions and include
testing strategies to mitigate failure in these areas. This testing
strategy should be operationalized in a testing framework that is
applied against the tool in a repeatable manner and the QA plans and
reports, as well as available indicators outlining the level and
coverage of testing should be available for review.

### Product Information and Documentation {#product_information_and_documentation}

Shelf-ready tools should differentiate the product information and
documentation artifacts and cater to the required audiences. Product
information should outline in a summary form the key functions and value
proposition of the tool and serve as a âquick accessâ document for
decision makers to understand the value proposition and value gained
from the tool (the brochure, so to say). In addition, Product
Documentation for shelf-ready goods should be comprehensive and
inclusive of all aspects to support an effective and safe implementation
and ongoing operations of the tool in the field. Product documentation
should include not only developer documentation (software design,
patterns, etc.), but also implementer documentation (installation
guides, architectural implementation patterns for scale, implementation
validation checks, etc.), administrator guides (configuration option and
descriptions of all features and options, etc.), user guides and
operation manuals (outlining the functionality of the system as well as
how it operates).

## Supports standards for data exchange as appropriate for the tool and aligned with the OpenHIE architecture {#supports_standards_for_data_exchange_as_appropriate_for_the_tool_and_aligned_with_the_openhie_architecture}

Shelf-ready software tools are well categorized within the business
functional domain or as a registry/metadata service or point-of-service
solution and, as such, adhere to clearly defined data exchange patterns
and flows. The solutions are well aligned to the OpenHIE architecture
and facilitate the required interactions to support the key use-cases
that are proposed and advertised as supported by the technology. As an
example, Point of Services systems interacting with patients would be
well suited to register and query patients and associated demographics
with a client registry and should be able to synchronize health facility
lists with a Facility Registry.

## Aligns with DevOps and Cloud-Services Guidelines {#aligns_with_devops_and_cloud_services_guidelines}

Shelf-ready tools and technologies look to ensure that they are aligning
to emerging guidelines such as the [DevOps and Cloud-Services
guidelines](https://docs.google.com/document/d/1daVn-xxxuhQvFzA4sIY2vsDnJxh7AV8DxbB8wkvZNpg/edit?usp=sharing).
These look to provide guidance on some of the major areas of
consideration for the deployment of implementations within and for
countries. These considerations often require a migrating path from
local hosting to international cloud services. Shelf-ready global goods
should provide a change management path/guideline for the transition
from local data centers to cloud, and take into account the need to
harmonize on a common approach to DevOps across digital health tools.
