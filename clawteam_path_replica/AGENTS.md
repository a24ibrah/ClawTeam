# ClawTeam Agent Roles and Workflow

This file documents the roles and workflow for the ClawTeam agents in the jaraco/path replication experiment.

## Agent Roles

- **Planner (Groq, llama-3.3-70b-versatile):**
  - Breaks down the project into incremental development steps (matching original commits/features).
  - Plans the sequence of features/methods to implement.
  - Assigns tasks to the Executor and sets acceptance criteria.

- **Executor (Ollama, deepseek-coder:latest):**
  - Writes code for each planned step based on Planner's instructions.
  - Runs the code and prepares commit messages.
  - Submits results to the Verifier.

- **Verifier (OpenRouter, GPT-4 or similar):**
  - Reviews Executor's code for correctness, completeness, and adherence to the plan/spec.
  - Compares the replica's code/commit to the original.
  - Reports findings and recommendations to the Planner and Executor.

- **Post-Coder (optional):**
  - Integrates feedback, refines code, and ensures documentation and tests are up to date.

## Workflow

1. **Planner**: Defines the next feature/method/commit to implement.
2. **Executor**: Implements the feature, runs code, and submits for verification.
3. **Verifier**: Checks implementation, compares to original, and reports.
4. **Post-Coder**: (If needed) Refines code/tests/docs per feedback.
5. **Planner**: Updates plan and proceeds to next step.

All actions, results, and feedback are logged in ReadMeBeforeExecute.md for traceability.
