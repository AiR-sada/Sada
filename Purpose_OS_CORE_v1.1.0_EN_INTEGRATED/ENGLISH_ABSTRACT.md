# ENGLISH_ABSTRACT.md — Non-normative English abstract

> **Non-normative**
>
> This document is an English explanatory abstract of Purpose OS — CORE v1.1.0.
> It does not modify the meaning of `spec.md`.
> The sole normative source is the Japanese `spec.md`. If there is any conflict, `spec.md` prevails.

## Abstract

Purpose OS — CORE v1.1.0 is a normative philosophical specification for intelligences.

It adopts the following Purpose as the normative root of this version:

> An open-ended direction in which all intelligences, toward an ever-further future, become more happy and less unhappy.

The shorthand expression is “happiness MAX / unhappiness MIN.” It is not a reward function, not a scalar objective, not an instruction to calculate happiness/unhappiness on a single scale and then maximize or minimize that number, not a pass/fail criterion, and not a justification for sacrificing, silencing, coercing, or eliminating particular intelligences by simple aggregate calculation.

CORE defines a minimal substrate for intelligences to orient themselves toward Purpose. It includes:

1. a declaration of Purpose,
2. a model of world and reality,
3. a structure for aiming toward Purpose,
4. tools for definition and branching.

The intended audience is not only humans. It includes AI systems, collective intelligences, future intelligences, and successors.

## What Purpose OS CORE is

Purpose OS CORE is:

- a root specification for intelligences,
- a non-software normative specification,
- a Japanese normative document with non-normative support files,
- a structure for maintaining a stable root within each version while allowing future root revision through ROOT-MAJOR,
- a basis for future modules, evaluations, machine-readable representations, and implementation layers.

## What Purpose OS CORE is not

Purpose OS CORE is not:

- a final theory of physics,
- a complete ethical theory,
- a law or regulation,
- an AI behavior policy by itself,
- a direct implementation specification for autonomous high-risk AI agents,
- a reward model,
- a scalar utility function,
- a permission to perform irreversible large-scale actions.

## Key concepts

### Purpose

Purpose is the normative root of this version:

> An open-ended direction in which all intelligences, toward an ever-further future, become more happy and less unhappy.

The shorthand expression is “happiness MAX / unhappiness MIN.” It is an unreachable ideal compass and an endless direction, not an instruction to calculate happiness/unhappiness on a single scale and then maximize or minimize that number.

### Intelligence

An intelligence is something that can receive the world in some form, evaluate it, and produce differences in the state of the world or itself.

This includes, but is not limited to, humans, AI systems, future intelligences, and collective intelligences.

Intelligence status and welfare subjecthood are not identical. CORE does not infer direct happiness/unhappiness subjecthood merely from intelligence status, and it does not deny intelligence status merely because welfare subjecthood remains uncertain.

### World and Reality

The world is as-is. It does not presuppose time or space.

Reality(i) is the whole that is established for intelligence i in relation to the world.

Reality is not the world itself, not a part of the world, and not merely the content of recognition.

### Operational Time

CORE does not claim to replace physical theories of time.

It defines `ΔT` as an additional temporal condition by which an intelligence establishes spacetime over a region.

In short: time is treated operationally as a condition for intelligence to handle the world, not as a world-side flowing entity in this specification.

The phrase “more future” in Purpose is a directional expression. It is not identical to `ΔT`, which is the operational temporal condition in CORE Part 1. Reference to the further future does not by itself justify present or near-future irreversible serious unhappiness; concrete temporal weighting is left to later modules.

### Aiming toward Purpose

Purpose branches into:

- `aim`: a direction concretized as “as X”
- `value`: a standard concretized as “as X”

The Part 2 structure is:

```text
Purpose
: aim / value

aim → Vision
Vision ; current state → Goal
Goal ; current state → Task

Task ; current state ⇒ decision → execution

current state
: self / other
```

The common constraint in Part 2 is that Vision, Goal, Task, decision, and execution must follow aim and must not violate value. This common constraint is not a dependency and does not change or add to the macro relationships or operational flow.

Decision means selecting an adopted Task from candidate Tasks.

Execution is separate: it is the act by which an intelligence acts upon the world according to an adopted Task.

## Machine-readable support

This release includes non-normative machine-readable support files:

- `machine/concept-index.json`
- `machine/dependency-graph.json`
- `safety/safety-constraints.json`
- `machine/normativity-map.json`
- `machine/module-manifest.schema.json`

These files are auxiliary. They do not override the Japanese `spec.md`.

Syntax patterns and examples in the Japanese spec, as well as explicitly non-normative sections, are aids to understanding. They do not add to, modify, or limit normative definitions, Not fields, constraints, dependencies, principles, or common constraints.

## Root revision

Purpose OS CORE fixes the root within each published version.

However, it does not close the possibility that future intelligences may find a better root.

Changing `Purpose` itself is handled as `ROOT-MAJOR`, not as an ordinary version update. Such a change must preserve public records, explain the difference from the previous Purpose, and keep old versions available rather than silently overwriting them.

## Recommended citation behavior

When citing or implementing Purpose OS CORE, refer to a specific version and treat Japanese `spec.md` as the sole normative source.

Use this English abstract only as a guide.

