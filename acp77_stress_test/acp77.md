# Potential Security Concerns and Threat Scenarios Introduced by ACP-77

## Overview

ACP-77 introduces significant changes to the Avalanche subnet ecosystem, including the separation of Subnet Validators from Primary Network Validators, a continuous fee mechanism, and enhanced sovereignty for Subnets. These changes aim to reduce barriers to entry and increase flexibility, but they also introduce potential security concerns. Identifying and addressing these concerns is critical to ensuring the robustness and reliability of the network.

### New Registration Flow

**Retrieve a BLS Multisig from the Subnet**: Subnets will define their own procedure for prospective validators to retrieve the necessary validator information.
**Issue a RegisterSubnetValidatorTx on the P-Chain**: This transaction will add the Subnet Validator to the Subnet's validator set on the P-Chain.
**SetSubnetValidatorWeightTx**: This transaction will modify the voting weight of a Subnet Validator and manage validator set updates.
**ExitValidatorSetTx**: Subnet Validators can exit the validator set without interacting with the Subnet, ensuring censorship resistance and validator autonomy.
**SetSubnetValidatorManagerTx:** Subnets will set the validator manager location, enabling the use of the new registration flow.
**IncreaseBalanceTx**: This transaction will allow anyone to add additional $AVAX to a Subnet Validator's balance.

### New Transactions Introduced in ACP-77

#### RegisterSubnetValidatorTx
#### SetSubnetValidatorWeightTx
#### ExitValidatorSetTx
#### SetSubnetValidatorManagerTx
#### IncreaseBalanceTx



## Potential Security Concerns

1. **Increased Number of Validators**
   - **Concern**: Lowering the cost and hardware requirements for becoming a Subnet Validator may lead to a significant increase in the number of validators. This can strain network resources, particularly the P-Chain.
   - **Threat Scenario**: Excessive memory and processing load on the P-Chain could lead to performance degradation or even denial-of-service (DoS) attacks if the system is overwhelmed by the number of validators.
   - **Mitigation**: Implement robust monitoring and scaling solutions to dynamically manage and allocate resources based on network load.

2. **Malicious Subnet Operators**
   - **Concern**: Subnets now have more control over their validator sets, which could be exploited by malicious operators.
   - **Threat Scenario**: A malicious Subnet operator could remove validators arbitrarily or manipulate validator weights to centralize control, potentially compromising the security and integrity of the Subnet.
   - **Mitigation**: Enforce transparent governance mechanisms within Subnets, and provide validators with tools to verify and audit Subnet operations before participating.

3. **Validator Exit Exploits**
   - **Concern**: Validators can exit the validator set and retrieve their remaining balance at any time, which could be exploited in specific scenarios.
   - **Threat Scenario**: Validators might collude to exit simultaneously, causing disruption in the Subnet’s operation or attempting to withdraw funds during a critical operation.
   - **Mitigation**: Implement penalties or cooldown periods for exits to discourage sudden or coordinated exits, and monitor for unusual exit patterns.

4. **Inadequate Bootstrapping Security**
   - **Concern**: The bootstrapping process for new validators relies on discovering and connecting to existing validators, which could be targeted by attackers.
   - **Threat Scenario**: An attacker could provide false bootstrap nodes, leading new validators to connect to malicious nodes that could manipulate or disrupt their initial state synchronization.
   - **Mitigation**: Use cryptographic proofs and trusted bootstrap nodes to ensure the authenticity and integrity of the bootstrapping process.

5. **Continuous Fee Mechanism Exploits**
   - **Concern**: The continuous fee mechanism introduces a new dynamic where validators must maintain a balance to stay active.
   - **Threat Scenario**: An attacker could manipulate fee dynamics or spam the network with microtransactions to force validators into inactivity or financial strain.
   - **Mitigation**: Implement rate limits and validation checks to prevent abuse of the fee mechanism, and establish clear guidelines for fee adjustments based on network conditions.

6. **Decentralization Trade-offs**
   - **Concern**: While the new system allows more validators, it might also lead to centralization if only a few validators end up dominating due to their resources.
   - **Threat Scenario**: A few powerful validators could dominate the network, reducing overall decentralization and increasing the risk of collusion or centralized control.
   - **Mitigation**: Promote decentralized participation by encouraging diverse validator sets and providing incentives for smaller validators.

### Stress Testing and Edge Cases

1. **Load Testing**
   - **Scenario**: Simulate a high number of validators joining and exiting the network simultaneously.
   - **Objective**: Assess the impact on the P-Chain's performance and stability under extreme load conditions.
   - **Expected Outcome**: Identify potential bottlenecks and implement optimizations to handle peak loads.

2. **Malicious Validator Simulation**
   - **Scenario**: Introduce validators with malicious intent to attempt arbitrary removals, weight manipulations, and coordinated exits.
   - **Objective**: Evaluate the effectiveness of governance and security mechanisms in detecting and mitigating malicious activities.
   - **Expected Outcome**: Enhance monitoring and response strategies to ensure network resilience against malicious actions.

3. **Fee Manipulation Testing**
   - **Scenario**: Test the continuous fee mechanism under various conditions, including fluctuating network activity and targeted fee manipulation attempts.
   - **Objective**: Ensure the fee mechanism remains fair and robust under different usage patterns and potential attacks.
   - **Expected Outcome**: Refine the fee calculation and enforcement process to prevent abuse and ensure sustainability.

4. **Bootstrapping Reliability**
   - **Scenario**: Conduct tests with different bootstrapping methods, including scenarios with compromised bootstrap nodes.
   - **Objective**: Verify the security and reliability of the bootstrapping process for new validators.
   - **Expected Outcome**: Implement stronger authentication and validation methods for bootstrap nodes.

5. **Governance Model Evaluation**
   - **Scenario**: Simulate various governance models within Subnets to test decision-making processes and dispute resolution.
   - **Objective**: Ensure that governance mechanisms are transparent, efficient, and resistant to manipulation.
   - **Expected Outcome**: Develop best practices for Subnet governance to maintain security and fairness.




## Using Simulations to Identify and Mitigate Security Concerns in ACP-77

Simulations can be a powerful tool to identify potential security concerns, understand the impact of different scenarios, and develop mitigation strategies for the changes introduced by ACP-77. By creating realistic models and running simulations, we can stress test the network, evaluate edge cases, and predict the behavior of the system under various conditions.

### Simulation Scenarios

#### 1. Load Testing

**Objective**: Assess the impact of a high number of validators joining and exiting the network simultaneously.

**Simulation Steps**:
1. **Initialize the Network**: Set up a simulated Avalanche network with a baseline number of validators and active Subnets.
2. **Simulate Validator Activity**:
   - **Joining**: Introduce a high volume of new validators joining the network at varying rates.
   - **Exiting**: Simulate a scenario where many validators exit the network simultaneously.
3. **Measure Metrics**:
   - Network latency
   - Transaction processing times
   - Resource utilization (CPU, memory)
   - Validator synchronization times
4. **Analyze Results**:
   - Identify performance bottlenecks
   - Evaluate the system's ability to handle peak loads
   - Determine any degradation in service or failures


#### 2. Malicious Validator Simulation

**Objective**: Evaluate the network's resilience against malicious validators attempting to disrupt the system.

**Simulation Steps**:
1. **Initialize the Network**: Set up a simulated network with standard validators and a few malicious validators.
2. **Malicious Actions**:
   - Arbitrary removals of other validators
   - Manipulation of validator weights
   - Coordinated exits to cause disruptions
3. **Monitor System**:
   - Detection of malicious activities
   - Response times to attacks
   - Impact on network stability and security
4. **Analyze Results**:
   - Effectiveness of governance and security mechanisms
   - Areas needing improvement in detection and mitigation


#### 3. Fee Manipulation Testing

**Objective**: Ensure the continuous fee mechanism remains robust under various conditions and potential manipulation attempts.

**Simulation Steps**:
1. **Initialize the Network**: Set up the network with validators and implement the continuous fee mechanism.
2. **Simulate Fee Dynamics**:
   - Normal operation with varying network activity
   - Targeted fee manipulation attempts (e.g., microtransactions to deplete validator balances)
3. **Measure Metrics**:
   - Fee stability over time
   - Impact on validator balances
   - Validator activity and inactivity rates
4. **Analyze Results**:
   - Identify potential vulnerabilities in the fee mechanism
   - Evaluate the fairness and robustness of fee calculations


#### 4. Bootstrapping Reliability

**Objective**: Verify the security and reliability of the bootstrapping process for new validators.

**Simulation Steps**:
1. **Initialize the Network**: Set up the network with existing validators and new validators attempting to join.
2. **Simulate Bootstrapping**:
   - Normal bootstrapping process
   - Compromised bootstrap nodes providing false information
3. **Monitor Process**:
   - Success rate of new validators joining the network
   - Time taken for successful bootstrapping
   - Detection of compromised nodes
4. **Analyze Results**:
   - Effectiveness of security measures during bootstrapping
   - Recommendations for improving bootstrapping security


#### 5. Governance Model Evaluation

**Objective**: Ensure that governance mechanisms within Subnets are transparent, efficient, and resistant to manipulation.

**Simulation Steps**:
1. **Initialize the Network**: Set up a network with Subnets implementing various governance models.
2. **Simulate Governance Processes**:
   - Proposal submissions and voting
   - Dispute resolutions
   - Parameter changes
3. **Measure Metrics**:
   - Time taken for decision-making processes
   - Participation rates in governance activities
   - Impact on network performance and security
4. **Analyze Results**:
   - Effectiveness and fairness of governance models
   - Recommendations for optimizing governance mechanisms


### Implementation Steps

1. **Define Simulation Parameters**:
   - Identify key parameters for each simulation scenario (e.g., number of validators, transaction rates, fee structures).
2. **Develop Simulation Models**:
   - Use cadCAD and radCAD to build detailed models representing the network, validators, and specific scenarios.
3. **Run Simulations**:
   - Execute simulations under different conditions to gather data on system behavior.
4. **Analyze Data**:
   - Use statistical and analytical tools to interpret simulation results and identify patterns, anomalies, and vulnerabilities.
5. **Develop Mitigation Strategies**:
   - Based on simulation results, propose and test mitigation strategies to address identified security concerns.

# Continuous Fee Mechanism

**Continuous Fee Mechanism:**
The core of ACP-77’s proposal is the replacement of the high upfront stake requirement with a continuous fee mechanism. Instead of requiring a large initial deposit, validators will pay ongoing fees to maintain their subnet validator registration on the P-Chain. This change aims to make the network more accessible by spreading the cost over time rather than demanding a large sum upfront​ (blocmates. | Crypto News & Information)​.

**Fee Calculation:**
The dynamic fee mechanism will be based on a target utilization of total subnet validators registered to the P-Chain, rather than the economic activity on the subnet itself. This means that the fees will adjust according to the number of validators, aiming to balance the network's load and resources efficiently​ (HelloARC)​.

**Impact on On-chain Costs:**
The proposed dynamic fee mechanism is designed to lower the hardware and maintenance costs for subnet validators. By reducing the requirement for validators to also validate the primary network’s C and X chains, hardware costs can be significantly reduced—from approximately $250 per month to around $80 per month per validator​ (blocmates. | Crypto News & Information)​.



## Validor weight adjustment
Through these dimensions, a standard charge that all Subnet Validators will pay will be calculated by the network based on network activity, commonly referred to as a "base fee". This base fee will move up when the total number of Subnet Validators is above target utilization and move down when the total number of Subnet Validators is below target utilization.
## Continuous fee mecanuism

# Nootes

Subnets can implement any mechanism they want to pay the continuous fee charged by the P-Chain for its participants.
Subnet creators have no restrictions on what requirements they have to join their Subnet as a validator.
How each Subnet handles stake associated with the Subnet Validator is entirely left up to the Subnet and can be treated independently to what happens on the P-Chain.
How to determine the weight of a validator? How this weight will increase or decreasee with stake chnaging? How slashing will impact the voting wweight?
How much continuus fee is paid by a validator? What is relation between activity and this fee? What is relation between rewards of subnet validator and this continuous fee?
Subnet creators should be aware that there is no notion of MinStakeDuration that is enforced by the P-Chain. It is expected that Subnets who choose to enforce a MinStakeDuration will lock the validator's Stake for the Subnet's desired MinStakeDuration.

fter this ACP is activated, the P-Chain will no longer support staking of any assets other than $AVAX for the Primary Network. The P-Chain will no longer support distribution of staking rewards for Subnets. All staking-related operations for Subnet Validation must be managed by the Subnet on the Subnet. The P-Chain simply requires a continuous fee per Subnet Validator. If a Subnet would like to manage their Validator's balances on the P-Chain, it can cover the cost for all Subnet Validators by posting the $AVAX balance on the P-Chain. Subnets can implement any mechanism they want to pay the continuous fee charged by the P-Chain for its participants.

y moving ownership of the Subnet's validator set from the P-Chain to the Subnet, Subnet creators have no restrictions on what requirements they have to join their Subnet as a validator. Any stake that is required to join the Subnet Validator set is locked on the Subnet. If a validator is removed from the Subnet Validator set via a SetSubnetValidatorWeightTx with weight 0 or an ExitValidatorSetTx on the P-Chain, the stake on the Subnet will continue to be locked. How each Subnet handles stake associated with the Subnet Validator is entirely left up to the Subnet and can be treated independently to what happens on the P-Chain.