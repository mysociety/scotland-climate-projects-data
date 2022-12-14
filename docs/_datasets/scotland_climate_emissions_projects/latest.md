---
name: scotland_climate_emissions_projects
title: Scotland Climate Emissions Projects
description: "Reformatted version of data published at https://sustainablescotlandnetwork.org/reports\n"
version: latest
licenses:
- name: CC-BY-4.0
  path: https://creativecommons.org/licenses/by/4.0/
  title: Creative Commons Attribution 4.0 International License
contributors:
- title: Sustainable Scotland Network
  path: https://sustainablescotlandnetwork.org/reports
  role: author
- title: mySociety
  path: https://mysociety.org
  role: author
custom:
  build: scotland_climate_projects_data.build:build_projects
  tests:
  - test_scotland_climate_emissions_projects
  dataset_order: 0
  download_options:
    gate: default
    survey: default
    header_text: default
  composite:
    xlsx:
      include: all
      exclude: none
      render: true
    sqlite:
      include: all
      exclude: none
      render: true
    json:
      include: all
      exclude: none
      render: true
  change_log:
    0.1.0: initial load of data
resources:
- title: Scotland Climate Emissions Projects
  description: "Reformatted version of data published at https://sustainablescotlandnetwork.org/reports\n"
  custom:
    row_count: 1673
  path: projects.csv
  name: projects
  profile: tabular-data-resource
  scheme: file
  format: csv
  hashing: md5
  encoding: utf-8
  schema:
    fields:
    - name: local-authority-code
      type: string
      description: 3/4 letter local authority code - see https://mysociety.github.io/uk_local_authority_names_and_codes/
      constraints:
        unique: false
      example: ABE
    - name: council
      type: string
      description: Local authority name
      constraints:
        unique: false
      example: Aberdeen City Council
    - name: start_year
      type: integer
      description: Year project started
      constraints:
        unique: false
        enum:
        - 2014
        - 2015
        - 2016
        - 2017
        - 2018
        - 2019
        - 2020
      example: 2014
    - name: end_year
      type: integer
      description: Year project ended
      constraints:
        unique: false
        enum:
        - 2015
        - 2016
        - 2017
        - 2018
        - 2019
        - 2020
        - 2021
      example: 2015
    - name: data_type
      type: string
      description: Type of data (all 'project' currently)
      constraints:
        unique: false
        enum:
        - project
      example: project
    - name: emission_savings
      type: string
      description: Estimated emission savings in tC02e/year
      constraints:
        unique: false
      example: '657'
    - name: project_name
      type: string
      description: Name of project
      constraints:
        unique: false
      example: Roll out of solar PV panels on 70 Council owned buildings.
    - name: lifetime
      type: string
      description: Project lifetime in years
      constraints:
        unique: false
      example: '5'
    - name: cost
      type: string
      description: Project cost in ??
      constraints:
        unique: false
      example: '1429517'
    - name: funding_source
      type: string
      description: Funding source for project
      constraints:
        unique: false
      example: "Part of the HyTrEc project\n(Hydrogen Transport Economy in the North\
        \ Sea Region)"
    - name: emission_source
      type: string
      description: Emissions sourcesfor project
      constraints:
        unique: false
      example: 'Grid Electricity '
    - name: annual_cost
      type: string
      description: Annual cost of project in ??
      constraints:
        unique: false
      example: '103000'
    - name: annual_savings
      type: string
      description: Annual savings from project in ??
      constraints:
        unique: false
      example: '23102'
    - name: measurement
      type: string
      description: Measurement of project
      constraints:
        unique: false
      example: Estimated
    - name: savings_start
      type: string
      description: Period savings start
      constraints:
        unique: false
      example: 2015/16
    - name: comments
      type: string
      description: Comments on project
      constraints:
        unique: false
      example: These projects aren't fully detailed as that information isn't collated
        in one place yet.
  hash: 95818dd62d55c6c143de70a4dc43b473
  download_id: scotland-climate-emissions-projects-projects
full_version: 0.1.0
permalink: /datasets/scotland_climate_emissions_projects/latest
---
