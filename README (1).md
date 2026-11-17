# Data protocol

No third-party dataset is needed. All generated data arise from `src/simulator.py` using a NumPy random generator. The generator creates seven-stage synthetic tool-order workflows with task constraints, a contextual stage-risk distribution, and zero or one semantic corruption per episode. No customer, web, personal or clinical data are used. Data fields are synthetic and do not identify real transactions.

Development IDs begin with `dev-` and test IDs with `test-`. Five thousand development examples are used only to choose checkpoint positions (exhaustive search over 35 three-stage subsets); 15,000 separate test examples are used only for evaluation. Test seeds and metadata are frozen in `configs/frozen_protocol.json`. The generator and outputs are included in the submission for auditing. Do not tune policy placement against held-out outcomes.

The experimental code, its generated cases, and its output may be adapted subject to any institutional course rules. External article PDFs are source documents, **not** part of the open synthetic dataset.
