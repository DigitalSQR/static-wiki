# Tupaia

Tupaia is an end-to-end data platform that supports data aggregation,
analysis and visualization for mapping health systems in low and
middle-income countries. Tupaia is used to complement other systems such
as DHIS2 and mSupply, utilizing several powerful features such as a data
broker that is able to seamlessly consume and route data from multiple
sources, the ability to support multiple data platforms and a highly
attractive GIS platform around which the visualizations are built.
Tupaia is completely free and open-source.

Tupaia combines data from multiple sources including DHIS2, mSupply,
Kobo, Tamanu and its own MediTrak app to help improve medicines
availability, map disease outbreaks, map public health programming,
undertake disease surveillance, respond to disasters and strengthen
service provision.

Tupaia MediTrak is a free and open-source data collection app, designed
specifically for the Pacific sub-region. Users can build their own
surveys, collect data offline across all question types, it has built-in
incentives to encourage users to collect data more frequently, along
with a newsfeed showing recently completed surveys and news items.

Tupaia is supported by a number of donors in the Pacific region,
including DFAT, UNFPA, World Bank and WHO. We also support the UNICEF
Laos Country Office and many smaller research institutes and
universities in the region. Tupaia is currently used across more than 12
countries in the region and consumes approximately 65,000 data points
each day.

### Approach

The primary functionality of Tupaia is to link together multiple data
sources to present a single, coherent view of a health system for
specific user groups. Originally designed to augment DHIS2 and mSupply,
the platform has grown to support end-to-end data pipelines, including
support for multiple data hierarchies, across multiple projects and
countries, with platform-wide SSO and highly granular roles-based
permissions. Also supports data exports to CSV, XLS and R, along with
PDF.

Tupaia is primarily used by healthcare workers and donors from low and
middle-income settings.

Tupaia User interfaces:

- Tupaia MediTrak
  - A data collection app with program and jurisdiction-based access
    user controls
  - React Native and available across iOS and Android.
  - Offline-first synchronizing system.
  - Each survey response has data and metadata (entity, time x 3,
    survey).
- Tupaia.org frontend
  - Main dashboard, map overlays and analytics user interface
  - React frontend
  - Map overlays
  - Dashboards with detailed insights/BI tools
  - Highly granular permissions system based on 4 data dimensions (Who,
    Where, What and When - Jane Smith could be granted access to TB data
    from Victoria and lose access on June 30th 2024).
  - Can download preconfigured reports in PDF, PNG and XLS/CSV filetypes
    straight from Tupaia.org frontend (efficient way to disseminate data
    and reports widely via permissions-based access, without needing to
    give all users access to the Admin Panel).
  - Uses Recharts for most dashboard elements, some custom-built
    visualizations
  - Uses Leaflet for most map overlays
  - Mapping layers can be pulled from any source, currently supports
    Mapbox and OpenStreetMaps
- Admin panel
  - React frontend
  - Connects to both the MediTrak server and the aggregation server.
  - Controls survey questions, bulk imports, data uploads and downloads
  - Main portal for tracking incoming data and outbreak management
  - User administration, authorizations & permissions
- Tupaia major backend components:
  - Aggregation server
    - PostGres
    - Fetches data and aggregates it.
    - Can fetch events or analytics
    - Analytics have a lot of possible aggregation types
  - Data broker
    - As the gateway to external (and internal) services, the data
      broker is the centrepiece of this project. Data from each
      jurisdiction will be processed through the data broker
    - Understands APIs and wrangles data to the consistent format we use
      internally
    - Both push and pull
  - MediTrak server
    - Now PostGres (previously a DHIS2 instance but this is now an
      external service)
    - Mothership for data collected through our services (via the app or
      admin panel)
    - Receives data in from our data collection app and the admin panel
    - Pushes data out via the data broker
  - Indicators engine
    - Specifies common concepts that are calculated from other data
    - Reduces error rates from needing to build out new algorithms for
      every report element or visualisation
    - Can pre-compile to save substantial processing time when calling
      up a visualisation or report (particularly useful for indicators
      compiling from large datasets)
    - Has access to aggregator and can pull data from any service
      (including from the indicators engine itself)
  - Data lake
    - Consumes and stores massive amounts of data in any format, with
      the ability to mirror and store external databases or consume only
      specified tables from external sources
    - Also supports storage of unstructured data
    - Transformations to our data model then occur on our side

### Implementations

Tupaia is used in 14 countries in the Indo-Pacific region.

### Resources

- Website: <https://tupaia.org>
- Documentation: <https://github.com/beyondessential/tupaia>
- Articles:
  - <https://www.beyondessential.com.au/tupaia-wins-at-commonwealth-digital-health-awards/>
  - <https://r4d.org/projects/tupaia-and-immunization-coverage-in-vanuatu/>
  - <https://www.unicef.org/innovation/stories/grantee-tupaia>
  - <https://indopacifichealthsecurity.dfat.gov.au/news-insights/foreign-minister-penny-wong-hears-about-ehealth-progress-samoa>
  - <https://sdgs.un.org/partnerships/tupaia>
