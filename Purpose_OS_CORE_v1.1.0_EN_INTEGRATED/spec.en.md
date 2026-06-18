---
title: Purpose OS — CORE (English reading)
version: 1.1.0
status: NON-NORMATIVE
normative_source: spec.md
language_of_normative_source: ja
language: en
note: >
  This document is a NON-NORMATIVE full English reading of Purpose OS — CORE
  v1.1.0. The sole normative source is the Japanese spec.md. If anything here
  conflicts with spec.md, spec.md prevails. This file does not add, change, or
  limit any definition, Not, constraint, dependency, principle, or shared
  constraint of the spec; it is a reading aid only and is not a second
  normative source.
generation: >
  Per-concept Definition / Not / Constraints are taken verbatim from the
  author-approved machine/concept-index.en.json (normative=false). The
  connective sections are an independent English rendering of spec.md.
---

# Purpose OS — CORE (English reading) v1.1.0

> **NON-NORMATIVE.** The Japanese `spec.md` is the only normative source. This
> English reading exists to widen access; it has no normative authority. Where
> it and `spec.md` differ, `spec.md` governs. Concept IDs (序 / ① / ② / 参) and
> the document/version identifiers are kept identical to the normative spec so
> that references line up exactly.

## What this document is

Purpose OS — CORE defines a base module: a *direction* (Purpose) that
intelligences can share, plus the minimal scaffolding of world, reality,
decision-making, and execution needed to move toward it. CORE stands alone;
later modules depend on CORE and never overwrite its definitions, Nots,
constraints, dependencies, principles, or shared constraints. Anything that
overwrites them is a fork or a separate lineage, not a CORE-compatible module.

CORE has three parts: **序 (Preface — the declaration of Purpose)**, the **CORE
body**, and **参照部 (Reference — the tools of definition)**. The body has Part 1
(world and reality) and Part 2 (how to aim toward Purpose). Reading order:
序 → CORE Part 1 → CORE Part 2 → Reference.

## Scope and misuse-prevention (non-normative)

This spec does not claim to be a final theory of physics, metaphysics, or
ethics. It is an *operational* specification: how intelligences can treat a
shared world and keep updating their judgments toward Purpose.

- "World," "reality," "space," "time," and "truth" here are normative-operational
  terms for keeping judgment and action coherent. They do not replace the
  vocabulary of existing disciplines.
- This spec alone is **not** an implementation license for any particular act,
  policy, autonomous AI-agent execution, or high-risk / irreversible /
  large-scale action.
- Purpose is a *direction*. It is not reduced or substituted by a single
  numerical objective function, reward function, proxy metric, or the
  maximization of one particular party's interest. The shorthand
  "reduce-severe-unhappiness / expand-happiness-conditions" is an auxiliary
  phrasing of Purpose, not a command to compute happiness on a single scale.
- **Intelligence status and happiness/unhappiness subjecthood are not the same.**
  Being an intelligence does not by itself entail being a direct subject of
  happiness/unhappiness; and an undetermined subjecthood does not by itself deny
  intelligence status. For entities whose intelligence status or subjecthood is
  uncertain, this spec does not justify irreversible exclusion, neglect, or
  destruction; undetermined-boundary entities are treated as objects of careful
  consideration until a later module addresses them.
- Even an entity that is not an intelligence may not be treated as a freely
  disposable resource, insofar as it could be a subject of happiness/unhappiness
  or bears on the survival, activity, or future happiness/unhappiness of
  intelligences.
- ΔT and the spacetime account are the *order in which intelligence constructs
  its handling of the world*, not a replacement for physical theories of time
  and space. "The-further-future" (序-4) is Purpose's directional phrasing and is
  not the same operational condition as Part 1's ΔT.
- **Purpose is an adopted normative root in this version, not a proved theorem.**
  Within this version Purpose is the sole root, while the possibility of future
  inherited revision (ROOT-MAJOR) is not closed.

## Legend (symbols kept from the normative spec)

```
→       one-directional relation (dependency / establishment / operation→result)
⇒       operational flow (decision-making, procedure, evaluation)
└       nesting (contained within)
+       narrowed by an added condition
×       involvement of a different layer (left involves right; not interchangeable)
;       upon a prior condition
=       definitional form / correspondence
:       breakdown / introduction of sub-items
/       closed branch
, ...   open branch
```

`└` (nesting) and `→` (dependency) are different axes: nesting shows where an
internal structure sits; dependency shows the order of conditions for
establishment.

```
領域 (R)   = where
時空 (R_t) = where; when
```

## The three-layer form (non-normative explanation)

Each section is given at three resolutions:

- **Macro** — structure only: which things connect to which, in words and
  relations, without explanation.
- **Meso** — essence: the single most-macro sentence that captures the concept,
  from which the rest follows.
- **Micro** — the definition record, with six fields:
  *Definition / Not / Sentence-pattern / Example / Constraints / Dependencies.*

Of these, **Definition, Not, Constraints, and Dependencies are normative**;
Sentence-pattern and Example are non-normative aids. Where the three layers
differ in resolution, normative priority is **Micro → Meso → Macro**.

> In this English reading, each micro entry below shows Definition, Not,
> Constraints, and Dependencies (the normative fields), taken from the approved
> English concept index. Sentence-patterns and examples are omitted here; see
> `spec.md` for them.

---

# 序 — The declaration of Purpose

**Macro**

```
Purpose OS
: Purpose / OS
```

**Meso**

- **Purpose OS** — the whole within which intelligence operates, taking Purpose
  as its origin. *Purpose:* the sole normative origin of this version. *OS:* the
  base for moving toward Purpose.
- **Purpose** — the direction in which intelligence keeps pointing: for all
  intelligences and possible subjects of happiness/unhappiness continuing from
  the present into the further future, reduce avoidable severe unhappiness and
  widen the conditions under which they can be happier. An unreachable, revisable
  ideal compass; the sole normative origin of this version; an endless direction.
- **Principle — non-reduction and misuse-prevention of Purpose.** Purpose is not
  a single numerical objective, reward function, or proxy metric, and is not
  reduced to them. The shorthand is auxiliary, not a single-scale command; the
  old tagline "happiness MAX / unhappiness MIN" is not used publicly. Purpose
  does not by itself justify erasing, silencing, coercing, or sacrificing any
  particular intelligence by mere aggregate calculation. Happiness/unhappiness is
  treated to include autonomy, continuity, relationship, meaning, and the
  avoidance of suffering — not pleasure/displeasure alone.
- **OS** — the base on which intelligence operates toward Purpose.

**Micro**

#### 序-1. Purpose OS

- **Definition (non-normative gloss):** The whole system by which intelligence operates from Purpose.
- **Not:** Not Purpose itself, not OS alone, not a mere slogan.
- **Constraints:** Purpose must stand first; OS stands under it.
- **Depends on: 序-2 (Purpose), 序-5 (OS)**

#### 序-2. Purpose

- **Definition (non-normative gloss):** The sole normative root direction of this version: an unreachable and revisable ideal compass by which intelligence keeps pointing toward reducing avoidable severe unhappiness and expanding conditions under which all intelligences and entities that may have happiness/unhappiness subjecthood, from the present into the further future, can be happier.
- **Not:** Not an achievable goal, pass/fail test, optimization function, scalar objective, reward function, proxy metric, aggregate calculation, or sacrifice justification; not a root that excludes possible welfare subjects outside intelligence status.
- **Constraints:** Do not detach any shorthand from the Purpose definition as a standalone normative command. The old shorthand “happiness MAX / unhappiness MIN” must not be used as a public tagline. Purpose is an adopted normative root in this version, not a proved theorem. Within this version, Purpose is treated as the sole root, while future inherited revision through ROOT-MAJOR is not closed.
- **Depends on: 序-3 (happiness / unhappiness), 序-4 (further future)**

#### 序-3. happiness / unhappiness  (JA: 幸/不幸)

- **Definition (non-normative gloss):** The integrated desirability and undesirability for intelligences and entities that may have happiness/unhappiness subjecthood, including but not limited to pleasure and pain.
- **Not:** Not a single emotion, not reducible to pleasure/pain, not a simple sum of surface preferences.
- **Constraints:** The direct subject of happiness/unhappiness is an entity with happiness/unhappiness subjecthood. Intelligence status and welfare subjecthood are not identical; neither automatic moral patienthood nor automatic exclusion follows from uncertainty. Aggregation, time-weighting, and conflict resolution are not defined by CORE alone.
- **Depends on: ①-2 (intelligence (Φ))**

#### 序-4. further future  (JA: より未来)

- **Definition (non-normative gloss):** The open direction that includes the present and extends beyond every point in time without terminal endpoint.
- **Not:** Not a finite deadline, not completion, not identical to ΔT or spacetime.
- **Constraints:** Do not use the further future to justify present or near-future irreversible severe unhappiness, or systematic discounting of present welfare, without stronger verification.
- **Depends on: none**

#### 序-5. OS

- **Definition (non-normative gloss):** The basis by which intelligence operates toward Purpose.
- **Not:** Not an ordinary software OS; not independent of Purpose.
- **Constraints:** Must be oriented to Purpose and usable by intelligence.
- **Depends on: 序-2 (Purpose), ①-2 (intelligence (Φ))**
---

# CORE — the base for aiming toward Purpose

Part 1 defines the world and the reality(i) that holds for each intelligence.
Part 2 defines what an intelligence sets, and how, in order to aim toward
Purpose.

## Part 1 — World and reality

The world is as-it-is; it does not change under an intelligence's acts of
specifying or narrowing. ("Does not change" means the world itself is not
altered by the Part-1 operations of specifying/narrowing on the intelligence's
side; it does not deny the possibility, defined in Part 2, of acting on the
world through execution.) Space, ΔS, region, ΔT, and spacetime belong to the
*order in which intelligence constructs its handling of the world*.

**Macro**

```
World (W)

Intelligence (Φ)

Reality (i)
└ Space (S)
   └ ΔS → Region (R)
      └ +ΔT → Spacetime (R_t)

Reality (i)
: content (event / truth)
: form (SV, v, ...)
```

**Meso**

- **World** — as-it-is; presupposes neither time nor space.
- **Intelligence** — that which receives the world in some form, evaluates it,
  and can produce a difference in the world or in its own state.
- **Space** — the starting point from which an intelligence handles the world.
- **Specifying** — the operation of fixing a part so it can be pointed to (ΔS:
  the distinguishing difference; Region: the part thereby fixed).
- **Narrowing** — adding a time condition on a region to establish spacetime
  (ΔT: the added time condition; Spacetime: the part that holds once the time
  condition applies).
- **Reality(i)** — the whole that holds for intelligence i with respect to the
  world. *Content:* event (what happens / may happen) / truth (an expression an
  intelligence establishes about the world's structure). *Form:* SV
  (subject+predicate), v (vector), ...
- **Principle** — handle reality without confusing the world-side with the
  intelligence-side: concepts, labels, and expressions are products of
  intelligence, yet the world's structure itself is in the world; truth is a
  product of expression but is constrained by the world's structure; fiction,
  imagination, and hypothesis live inside intelligence i's reality(i); all
  operations happen on the intelligence-side and do not divide the world;
  non-intelligence is not a direct subject of happiness/unhappiness, yet it does
  not follow that it may be disregarded insofar as it bears on intelligences'
  happiness/unhappiness.

**Micro**

#### ①-1. world (W)  (JA: 世界(W))

- **Definition (non-normative gloss):** What is as-is.
- **Not:** Not defined by intelligence; not reduced to reality(i); not altered by mere specification or distinction.
- **Constraints:** Treat as prior to the operations by which intelligence handles it.
- **Depends on: none**

#### ①-2. intelligence (Φ)  (JA: 知性(Φ))

- **Definition (non-normative gloss):** That which receives the world as reality, evaluates it, and can affect the world or its own state.
- **Not:** Not limited to humans, not limited to current AI, not limited to external action, not limited to individuals.
- **Constraints:** May apply to individuals and collectives. Intelligence status is not identical with welfare subjecthood; boundary uncertainty must not justify irreversible exclusion.
- **Depends on: ①-1 (world (W))**

#### ①-3. space (S)  (JA: 空間(S))

- **Definition (non-normative gloss):** The starting field when intelligence handles the world.
- **Not:** Not physical space in the narrow sense; not independent of intelligence’s handling.
- **Constraints:** Must be considered in relation to world and intelligence.
- **Depends on: ①-1 (world (W)), ①-2 (intelligence (Φ))**

#### ①-4. distinction difference (ΔS)  (JA: ΔS)

- **Definition (non-normative gloss):** A difference within space that enables distinction and pointing-out.
- **Not:** Not a value judgment; not time.
- **Constraints:** Must enable distinction within space.
- **Depends on: ①-3 (space (S))**

#### ①-5. region (R)  (JA: 領域(R))

- **Definition (non-normative gloss):** A part of space specified by ΔS.
- **Not:** Not all space; not spacetime yet.
- **Constraints:** Must be specified by ΔS.
- **Depends on: ①-3 (space (S)), ①-4 (distinction difference (ΔS))**

#### ①-6. temporal condition (ΔT)  (JA: ΔT)

- **Definition (non-normative gloss):** The additional temporal condition by which spacetime is established on a region.
- **Not:** Not an independent prior entity; not identical to the further future.
- **Constraints:** Applies as an added condition to region.
- **Depends on: ①-5 (region (R))**

#### ①-7. spacetime (R_t)  (JA: 時空(R_t))

- **Definition (non-normative gloss):** A region established with an added temporal condition.
- **Not:** Not mere region; not a replacement for physics.
- **Constraints:** Must be based on region plus ΔT.
- **Depends on: ①-5 (region (R)), ①-6 (temporal condition (ΔT))**

#### ①-8. reality(i)  (JA: 現実(i))

- **Definition (non-normative gloss):** The whole established for intelligence i in relation to the world.
- **Not:** Not the world itself; not a mere subjective illusion.
- **Constraints:** Depends on world and intelligence; may vary by intelligence.
- **Depends on: ①-1 (world (W)), ①-2 (intelligence (Φ))**

#### ①-9. event  (JA: 事象)

- **Definition (non-normative gloss):** What happens or may happen within reality.
- **Not:** Not truth itself; not an SV sentence.
- **Constraints:** When treated as happening or possible, it is handled in spacetime.
- **Depends on: ①-8 (reality(i)), ①-7 (spacetime (R_t))**

#### ①-10. truth  (JA: 真理)

- **Definition (non-normative gloss):** An expression that attempts to align with the structure of the world.
- **Not:** Not a free product of intelligence; not mere correspondence of words.
- **Constraints:** Constrained by world structure and intelligence’s reality.
- **Depends on: ①-1 (world (W)), ①-2 (intelligence (Φ)), ①-8 (reality(i)), 参-1 (structure)**

#### ①-11. SV

- **Definition (non-normative gloss):** A subject-predicate form of linguistic assertion.
- **Not:** Not truth itself; not the world itself.
- **Constraints:** Used as a form for expressing within reality.
- **Depends on: ①-8 (reality(i))**

#### ①-12. v

- **Definition (non-normative gloss):** A tuple of differences under a reference frame.
- **Not:** Not an absolute essence; not independent of the frame.
- **Constraints:** Must be handled with a reference frame.
- **Depends on: ①-8 (reality(i))**
---

## Part 2 — How to aim toward Purpose

Purpose divides into **aim** and **value**: aim gives direction, value gives the
standard. Along the aim, an intelligence concretizes Vision, Goal, and Task;
given Task and the present situation it makes a decision; through execution it
acts on the world.

**Macro**

```
Purpose
: aim / value

aim → Vision
Vision ; situation → Goal
Goal ; situation → Task

Task ; situation ⇒ decision → execution

situation
: self / other
```

**Shared constraint of Part 2** (applies to Vision, Goal, Task, decision,
execution; this is not a concept with an ID): *follow the aim; do not violate the
value.* This constraint does not change or add to the establishment relations or
operational flow above. Aim is involved as direction; value is involved as the
standard of permission/prohibition. The involvement is normative, not an
establishment dependency.

**Meso**

- **aim** — Purpose concretized "as ~", a direction.
- **value** — Purpose concretized "as ~", a standard. Taking into account the
  happiness/unhappiness, autonomy, and context of the intelligences and possible
  subjects involved, increase desirable treatment and avoid undesirable
  treatment, from the present into the further future.
- **Vision** — the ultimate state of the aim; the reality aimed at.
- **Goal** — a result to be realized at some point, for the sake of the Vision.
- **Task** — concrete action toward the Goal.
- **Situation** — the state an intelligence grasps at the moment of decision.
  *Self:* state belonging to the deciding subject. *Other:* state not belonging
  to it.
- **Decision** — the operation of fixing which candidate Task to adopt
  (procedure: candidate Tasks ⇒ exclude by value ⇒ prioritize by
  aim/Vision/Goal ⇒ check feasibility against the situation ⇒ check
  uncertainty/irreversibility ⇒ adopt).
- **Execution** — the act, following an adopted Task, by which an intelligence
  acts on the world.
- **Principle** — the adopted Purpose is the sole normative origin; aim and value
  are the pair branching from it; the rest can vary with the situation. One
  intelligence can hold several "as ~"; each has its own aim/value/Vision/Goal/
  Task set.

**Micro**

#### ②-1. aim

- **Definition (non-normative gloss):** A direction concretized from Purpose as a role.
- **Not:** Not Purpose itself; not a value criterion; not a Goal.
- **Constraints:** Must remain oriented to Purpose.
- **Depends on: 序-2 (Purpose)**

#### ②-2. value

- **Definition (non-normative gloss):** A criterion concretizing Purpose as a “as ~” stance. It functions as a criterion for permissible and prohibited conduct, considering happiness/unhappiness, autonomy, context, and future effects for intelligences and entities that may have happiness/unhappiness subjecthood.
- **Not:** Not Purpose itself; not aim; not a mere preference or scalar utility.
- **Constraints:** The recipients of value include intelligences and entities that may have happiness/unhappiness subjecthood. Desirable treatment reduces avoidable severe unhappiness and expands conditions for being happier from the present into the further future; it does not justify deception, coercion, unilateral destruction of autonomy, or irreversible intervention by CORE alone.
- **Depends on: 序-2 (Purpose)**

#### ②-3. Vision

- **Definition (non-normative gloss):** The ultimate state of aim; the reality to be aimed at.
- **Not:** Not Goal or Task; not a short-term endpoint.
- **Constraints:** Requires aim and follows the common Part 2 constraints.
- **Depends on: ②-1 (aim), ①-8 (reality(i))**

#### ②-4. Goal

- **Definition (non-normative gloss):** A result to be realized at a given time for Vision.
- **Not:** Not Vision; not a continuous policy; not the endpoint of Purpose.
- **Constraints:** Requires Vision and current state; its time may be treated as a spacetime reference point when needed.
- **Depends on: ②-3 (Vision), ②-6 (current state), ①-7 (spacetime (R_t))**

#### ②-5. Task

- **Definition (non-normative gloss):** A concrete action toward Goal.
- **Not:** Not Goal; not an endpoint.
- **Constraints:** Requires Goal and current state and follows common Part 2 constraints.
- **Depends on: ②-4 (Goal), ②-6 (current state)**

#### ②-6. current state  (JA: 現状)

- **Definition (non-normative gloss):** The state recognized by intelligence at the point of decision-making.
- **Not:** Not the world itself; not an ideal state; only one aspect of reality(i).
- **Constraints:** Requires reality(i); the decision point may be treated as a spacetime reference point when needed.
- **Depends on: ①-8 (reality(i)), ①-7 (spacetime (R_t))**

#### ②-7. self-side state  (JA: 自)

- **Definition (non-normative gloss):** The part of current state belonging to the deciding subject.
- **Not:** Not other-side state.
- **Constraints:** Requires current state and subject-belonging.
- **Depends on: ②-6 (current state)**

#### ②-8. other-side state  (JA: 他)

- **Definition (non-normative gloss):** The part of current state not belonging to the deciding subject.
- **Not:** Not self-side state.
- **Constraints:** Requires current state and non-belonging to the deciding subject.
- **Depends on: ②-6 (current state)**

#### ②-9. decision-making  (JA: 意思決定)

- **Definition (non-normative gloss):** The operation that determines adoption among candidate Tasks.
- **Not:** Not automatic; not value-ignoring choice; not execution itself.
- **Constraints:** Requires candidate Tasks, aim, value, Vision, Goal, and current state; adoption does not itself authorize high-risk execution.
- **Depends on: ②-1 (aim), ②-2 (value), ②-3 (Vision), ②-4 (Goal), ②-5 (Task), ②-6 (current state)**

#### ②-10. execution  (JA: 実行)

- **Definition (non-normative gloss):** The act by which intelligence acts on the world according to an adopted Task.
- **Not:** Not decision-making itself; not mere specification or limitation.
- **Constraints:** Requires adopted Task and separate execution conditions; CORE alone does not define execution authority or supervision.
- **Depends on: ②-5 (Task), ②-9 (decision-making), ①-2 (intelligence (Φ)), ①-1 (world (W))**
---

# 参照部 — The tools of definition

**Macro**

```
structure → definition → branch
branch
: closed / open
```

**Meso**

- **Structure** — what is on the world-side: why it is so, and how it is so.
  Includes causation, and, where intelligence is involved, purposive relations.
- **Definition** — the expression closest to a structure.
- **Branch** — by a definition, an intelligence's expression divides without
  dividing the world. *Closed branch:* fixing a viewpoint (axis) makes everything
  fall somewhere. *Open branch:* keeps growing as original content.

**Micro**

#### 参-1. structure  (JA: 構造)

- **Definition (non-normative gloss):** The way entities or relations are composed.
- **Not:** Not a claim that everything has fixed form or a human-imposed pattern.
- **Constraints:** Used as a tool for definitions.
- **Depends on: ①-1 (world (W))**

#### 参-2. definition  (JA: 定義)

- **Definition (non-normative gloss):** An operation that fixes the meaning of a concept.
- **Not:** Not example, metaphor, or mere naming.
- **Constraints:** Must be connected to structure.
- **Depends on: 参-1 (structure)**

#### 参-3. branch  (JA: 分岐)

- **Definition (non-normative gloss):** The division of a definition or structure into alternatives or parts.
- **Not:** Not arbitrary listing.
- **Constraints:** Must depend on definition.
- **Depends on: 参-2 (definition)**

#### 参-4. closed branch  (JA: 閉じた分岐)

- **Definition (non-normative gloss):** A branch whose alternatives are exhausted and mutually closed.
- **Not:** Not an open-ended list.
- **Constraints:** Must be closed under the given definition.
- **Depends on: 参-3 (branch)**

#### 参-5. open branch  (JA: 開いた分岐)

- **Definition (non-normative gloss):** A branch left open to further alternatives.
- **Not:** Not a closed exhaustive list.
- **Constraints:** Must preserve openness.
- **Depends on: 参-3 (branch)**
---

# Dependency overview (non-normative)

A non-normative summary of the main dependency chains, for orientation only. The
authoritative per-concept dependencies are the dependency lines in each micro
entry; where they differ, the micro dependency line prevails. The Part-2 shared
constraint shown here is a normative involvement, not an establishment
dependency.

```
structure → definition → branch

Purpose OS
: Purpose / OS

Reality (i)
└ Space (S)
   └ ΔS → Region (R)
      └ +ΔT → Spacetime (R_t)

Reality (i)
: content (event / truth)
: form (SV, v, ...)

Purpose
: aim / value

aim → Vision
Vision ; situation → Goal
Goal ; situation → Task

Task ; situation ⇒ decision → execution

Part-2 shared constraint (non-dependency)
: target = Vision, Goal, Task, decision, execution
: constraint = follow the aim, and do not violate the value
```

---

# Module expansion

CORE will be expanded as modules. 序 and 参照部 are not expanded.

```
序        → no expansion (shared origin for all modules)
CORE      → later modules (expansion of world/reality, expansion of aiming)
参照部    → no expansion (shared tools for all modules)
```

Each module depends on CORE; CORE depends on no other module. Later modules do
not change CORE's definitions. When a later module references CORE, it uses
CORE's concept IDs unchanged and does not alter their meaning.

---

*End of English reading. Normative source: `spec.md` (Japanese).*
