# Quantative Subnet Launch Framework

### Design Choices for Subnet Creators Post-ACP-77

Post-ACP-77, subnet creators on the Avalanche network have a range of design choices to consider when launching and managing a subnet. Here are the key design choices:

### Validator Set Configuration

1. **Validator Selection:**
   - **Criteria for Validators:** Decide on the criteria for validators, such as technical specifications, stake requirements, and geographical distribution.
   - **Number of Validators:** Determine the optimal number of validators needed to balance security and decentralization with operational efficiency.

2. **Staking Requirements:**
   - **Minimum Stake:** Set the minimum amount of tokens that validators need to stake to participate in the subnet.
   - **Staking Token:** Choose the native token for staking and decide if it will be the subnet's own token or AVAX.

3. **Reward Mechanisms:**
   - **Reward Distribution:** Design the reward distribution mechanism for validators, including how rewards are calculated and distributed.
   - **Incentives:** Develop incentives to encourage honest behavior and long-term participation from validators.

### Economic and Fee Structures

4. **Continuous Fee Mechanism:**
   - **Fee Rates:** Determine the dynamic base fee rate that validators will pay to the P-Chain based on network activity.
   - **Balance Management:** Implement strategies for validators to manage their balance and ensure they do not run out of funds to cover continuous fees.

5. **Economic Models:**
   - **Tokenomics:** Develop the overall economic model for the subnet, including token issuance, distribution, and utility within the subnet.
   - **Sustainability:** Ensure the economic model is sustainable and attractive to both validators and users.


6. **Security Measures:**
   - **Validator Integrity:** Implement measures to ensure validator integrity, including slashing mechanisms for misbehavior.
   - **Security Protocols:** Define the security protocols and practices to protect the subnet from attacks.


## 1. Validator Set Configuration Simulator

**Validator Selection:**
- **Criteria Input:** Allow users to define technical specifications, geographic distribution, and reputation criteria for validators.
- **Simulation Output:** Generate potential validator sets based on input criteria, displaying diversity, technical capability, and reputation scores.

**Staking Requirements:**
- **Input Variables:** Minimum stake, staking token type (AVAX or custom token).
- **Simulation Output:** Display the impact of different staking requirements on validator participation and network security.

**Reward Mechanisms:**
- **Configuration Options:** Allow users to set block rewards, transaction fees, and performance-based incentives.
- **Simulation Output:** Calculate and display projected validator rewards based on the configuration.

#### 2. Economic Model Simulator

**Continuous Fee Mechanism:**
- **Fee Rate Inputs:** Allow users to set dynamic base fee rates and balance management strategies.
- **Simulation Output:** Show the impact of different fee rates on validator profitability and network sustainability.

**Tokenomics:**
- **Supply and Distribution:** Let users define total token supply, initial distribution, and utility.
- **Simulation Output:** Display the projected economic activity and token value over time.

**Sustainability Analysis:**
- **Incentive Structures:** Simulate the long-term impact of various incentive structures on network participation and economic health.

#### 3. Security

**Validator Integrity:**
- **Slashing Conditions:** Allow users to set slashing conditions for different types of validator misbehavior.
- **Simulation Output:** Show the effect of slashing on network security and validator behavior.

### Example Use Case

A subnet developer wants to create a DeFi platform on Avalanche. They use the tool to:
- Define technical specifications and staking requirements for validators.
- Set reward mechanisms and continuous fee rates.
- Simulate the economic model to ensure sustainability.
- Configure slashing conditions and governance rules.
- View simulation results to make informed design choices.

By using this tool, subnet developers can make data-driven decisions, optimize their subnet configurations, and enhance the security, performance, and economic viability of their networks.

## Quantitative Subnet Launch Framework: Simulation Engine

To create an effective simulation engine for subnet developers on the Avalanche network, we will focus on three main modules: Validator Set Configuration Simulator, Economic Model Simulator, and Security Simulator. Each module will provide inputs and generate outputs to help developers make informed decisions.

#### 1. Validator Set Configuration Simulator

**Validator Selection:**
- **Criteria Input:**
  - **Technical Specifications:** CPU, RAM, storage, and network bandwidth.
  - **Geographic Distribution:** Regions or continents to ensure diversity.
  - **Reputation Criteria:** Historical performance, uptime, and trust scores.
- **Simulation Output:**
  - **Validator Set:** List of validators that meet the criteria.
  - **Diversity Score:** Measure of geographic and technical diversity.
  - **Reputation Score:** Aggregate score based on input criteria.

**Staking Requirements:**
- **Input Variables:**
  - **Minimum Stake:** Number of tokens required.
  - **Staking Token Type:** AVAX or custom token.
- **Simulation Output:**
  - **Participation Rate:** Percentage of validators willing to stake the minimum amount.
  - **Security Level:** Impact of staking requirements on network security.

**Reward Mechanisms:**
- **Configuration Options:**
  - **Block Rewards:** Tokens per block.
  - **Transaction Fees:** Percentage of fees shared with validators.
  - **Performance Incentives:** Bonuses for high uptime and performance.
- **Simulation Output:**
  - **Projected Rewards:** Expected earnings for validators based on configuration.
  - **Incentive Effectiveness:** Impact of rewards on validator behavior and participation.

#### 2. Economic Model Simulator

**Continuous Fee Mechanism:**
- **Fee Rate Inputs:**
  - **Base Fee Rate:** Initial fee per validator.
  - **Dynamic Adjustments:** Rules for adjusting fees based on network activity.
  - **Balance Management:** Strategies for maintaining sufficient balance.
- **Simulation Output:**
  - **Validator Profitability:** Impact of fee rates on validator earnings.
  - **Network Sustainability:** Long-term effects on network operations and health.

**Tokenomics:**
- **Supply and Distribution:**
  - **Total Token Supply:** Initial and maximum supply.
  - **Initial Distribution:** Allocation to validators, developers, community, etc.
  - **Utility:** Use cases for the token within the subnet.
- **Simulation Output:**
  - **Economic Activity:** Projected transaction volume and value.
  - **Token Value:** Estimated token price over time based on supply and demand.

**Sustainability Analysis:**
- **Incentive Structures:**
  - **Staking Rewards:** Frequency and amount.
  - **Participation Bonuses:** Extra rewards for early or continuous participation.
- **Simulation Output:**
  - **Network Participation:** Long-term validator and user engagement.
  - **Economic Health:** Overall financial stability and growth prospects.

#### 3. Security Simulator

**Validator Integrity:**
- **Slashing Conditions:**
  - **Double-Signing:** Penalty for signing conflicting blocks.
  - **Downtime:** Penalty for extended periods of inactivity.
  - **Malicious Activity:** Other forms of misbehavior.
- **Simulation Output:**
  - **Security Level:** Impact of slashing on network security.
  - **Validator Behavior:** Changes in validator behavior due to slashing risks.

### Simulation Engine Implementation

#### Validator Set Configuration:

Use probabilistic models to simulate the selection of validators based on input criteria.
Calculate participation rates and security scores using statistical methods.

#### Economic Model Simulation:
Implement economic models to simulate token distribution, transaction fees, and validator rewards.
Use differential equations to project token supply and value over time.

#### Security Simulation:
Develop algorithms to simulate validator behavior and slashing events.
Use game theory to model validator incentives and potential misbehavior scenarios.

#### Data Processing:
**Input Handling:** Parse and validate user inputs to ensure they are within acceptable ranges and formats.
Output Generation: Use the simulation results to generate detailed reports and visualizations.

python simulation_engine/cli.py validator examples/example_validator_config.json
python simulation_engine/cli.py economic examples/example_economic_model.json
python simulation_engine/cli.py security examples/example_security_model.json
