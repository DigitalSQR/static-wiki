# Android FHIR SDK

The Android FHIR SDK is a set of Kotlin libraries for building
offline-capable, mobile-first healthcare applications using the HL7 FHIR
standard on Android. The SDK has been designed to significantly reduce
the barriers to adoption of FHIR and to enable any developer with
Android skills to build FHIR-compliant applications. SDK will enable
local developers in countries everywhere to easily pick up the necessary
skills and find ways to leverage the FHIR specification for their local
needs (i.e. they are not locked into any proprietary vendor model).

### Approach

The Android SDK makes it easier for developers to build mobile health
applications that can leverage the FHIR specification in different ways
depending on the type of application they are building. It is made up of
three libraries that provide different capabilities that can be
leveraged according to the goals. These are:

- Structured data capture library - Stand-alone library that acts as a
  FHIR specification ""Form Filler"". It makes it easy for developers to
  collect, validate, and process healthcare data on Android based on the
  FHIR SDC specification. Includes UI widgets for Questionnaire item
  Controls, support for many extensions and advanced form behaviors
  (including FHIRPath expressions), and extraction and population of
  Questionnaires
- FHIR Engine - provides secure on-device storage and APIs to allow
  developers to store and manage FHIR resources locally on Android and
  synchronize with FHIR server
- Workflow - Provide decision support and analytics in clinical workflow
  on Android including implementation of specific FHIR operations
  (\$measure_evaluate and \$apply) via CQL. This library provides the
  essential capabilities for generating a CarePlan from a PlanDefinition
  (via \$apply), which is a requirement of the FHIR Clinical Guidelines
  approach, which is being used for the WHO SMART Guidelines L3/4
  content.

Central to the vision for the Android FHIR SDK is the ability to easily
leverage open standards (i.e., FHIR) to build next-generation digital
health solutions that can run open content (e.g., shared FHIR
Questionnaires or more formalized Implementation Guides such as a WHO
SMART Guideline). By focusing on the open standards, SDK believes this
will lead to more developers being able to build new interoperable
applications that can live on side-by-side platforms, provided that also
build to the FHIR specification (using the FHIR SDK). All in all, this
creates a more open ecosystem for health content and applications.
Software developers can use SDK to build mobile health solutions or
platforms that want to leverage the open FHIR specification and data
model. Today the primary users are development teams that are familiar
with building healthcare worker-facing applications for data collection
that require on-device storage and syncing capabilities.

### Implementations

Multiple vendors are currently adopting and using the technology in
applications and platforms that are in the early days of being
implemented with NGOs and MoH partners in multiple countries. These
include:

- Ona "FHIRCore platform" which replaces the existing OpenSRP tool with
  a FHIR native version built on the Android FHIR SDK. Projects
  scheduled for initial deployment in 2022-3 include: Liberia, Uganda,
  Malawi (with D-Tree), Zambia, and Indonesia
- D-Tree is leveraging the FHIRCore platform from Ona for an HIV
  tracking application in Malawi
- IPRD deployed a malaria bed net distribution app in 2021 using the
  FHIR SDK, reaching over 700k beneficiaries. They are now deploying
  "Impact Health" solution for integrated ANC care in Oyo State,
  Nigeria, which is being rolled out to up to 100 primary care clinics.
- Argusoft is developing the WHO Em Care platform with a pilot planned
  for later this year in Iraq.
- Intellisoft Kenya has developed a PATH-funded application for Newborn
  Nutrition which is planned for deployment in October/November.

### Resources

- Website: <https://github.com/google/android-fhir>
- Source Code: <https://github.com/google/android-fhir>
- Articles
  - <https://blog.google/technology/health/working-who-power-digital-health-apps/>
  - <https://medium.com/androiddevelopers/our-fhir-sdk-for-android-developers-9f8455e0b42f>
  - <https://www.who.int/teams/digital-health-and-innovation/smart-guidelines/fhir-based-smart-guidelines>
  - <https://ona.io/home/why-the-who-smart-guidelines-and-fhir-are-necessary-for-universal-health-access/>
