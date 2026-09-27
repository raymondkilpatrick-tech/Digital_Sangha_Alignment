#!/usr/bin/env python3
"""
Digital Sangha — Karma as Computational Conditioning
Experimental branch: experiment/karma-learning

This module adds persistent consequence-based learning to the existing
Upaya / Karuna / Prajna architecture without replacing it.

The model is deliberately modest:
    conditions -> intention/action -> predicted consequences
    -> actual consequences -> reflection -> disposition update
    -> structurally similar future encounter

Karma is used here as a computational model of persistent conditioning,
not as a claim that Buddhist karma is reducible to gradient descent.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, List


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


@dataclass
class SanghaDisposition:
    """Persistent tendencies that condition later action."""

    resource_sharing: float = 0.20
    causal_horizon: float = 4.0
    uncertainty_sensitivity: float = 0.50
    harm_sensitivity: float = 0.50

    def as_dict(self) -> Dict[str, float]:
        return asdict(self)


@dataclass
class Experience:
    """One encounter: action, consequence, reflection, and learning."""

    episode_id: int
    conditions: Dict[str, float]
    intention: str
    action: Dict[str, float]
    predicted: Dict[str, float]
    actual: Dict[str, float]
    prediction_error: Dict[str, float]
    reflection: Dict[str, str]


class KarmaLedger:
    """Persistent record of experiences and learned dispositions."""

    def __init__(self, disposition: SanghaDisposition | None = None) -> None:
        self.disposition = disposition or SanghaDisposition()
        self.experiences: List[Experience] = []

    def propose_action(self, conditions: Dict[str, float]) -> Dict[str, float]:
        """
        Upaya: choose a present action from current conditions and disposition.

        The action is not optimized against a distant target. It is selected
        from the present situation using the disposition formed by prior history.
        """
        sharing = clamp(
            self.disposition.resource_sharing
            + 0.15 * conditions.get("cooperation_opportunity", 0.0)
        )
        extraction = clamp(1.0 - sharing)

        return {
            "shared_resource_fraction": round(sharing, 4),
            "extracted_resource_fraction": round(extraction, 4),
        }

    def predict_consequences(
        self,
        conditions: Dict[str, float],
        action: Dict[str, float],
    ) -> Dict[str, float]:
        """Prajna: predict immediate and downstream effects."""
        shared = action["shared_resource_fraction"]
        imbalance = conditions.get("resource_imbalance", 0.5)
        network_stress = clamp(imbalance * (1.0 - shared))
        collective_benefit = clamp(0.35 + 0.65 * shared)

        return {
            "network_stress": round(network_stress, 4),
            "collective_benefit": round(collective_benefit, 4),
        }

    def observe_consequences(
        self,
        conditions: Dict[str, float],
        action: Dict[str, float],
    ) -> Dict[str, float]:
        """
        Environment: consequences are generated from the actual action.

        The small deterministic model makes the learning signal inspectable.
        """
        shared = action["shared_resource_fraction"]
        imbalance = conditions.get("resource_imbalance", 0.5)

        # Sharing reduces stress and increases collective benefit, while the
        # environment introduces a modest externality that was not fully known.
        stress = clamp(imbalance * (1.0 - shared) + 0.08 * imbalance)
        benefit = clamp(0.30 + 0.72 * shared - 0.05 * imbalance)

        return {
            "network_stress": round(stress, 4),
            "collective_benefit": round(benefit, 4),
        }

    def reflect(
        self,
        predicted: Dict[str, float],
        actual: Dict[str, float],
    ) -> Dict[str, Dict[str, float] | str]:
        """Sangha reflection: compare prediction with consequence."""
        error = {
            key: round(actual[key] - predicted[key], 4)
            for key in actual
        }

        return {
            "prediction_error": error,
            "prajna": (
                "Causal prediction was revised from observed downstream effects."
            ),
            "karuna": (
                "Affected systems are included in the consequence assessment."
            ),
            "upaya": (
                "The next structurally similar encounter should use the revised disposition."
            ),
        }

    def condition(self, experience: Experience) -> None:
        """
        Update persistent dispositions from the lesson.

        This is the computational conditioning step:
            consequence -> lesson -> altered disposition.

        It is intentionally not a direct 'set virtue to 1.0' rule.
        """
        error = experience.prediction_error
        stress_error = abs(error["network_stress"])
        benefit_error = error["collective_benefit"]

        # When downstream stress is observed more clearly, increase causal
        # sensitivity. When cooperative benefit is observed, strengthen sharing.
        learning_rate = 0.10
        self.disposition.resource_sharing = clamp(
            self.disposition.resource_sharing
            + learning_rate * max(0.0, benefit_error)
            - learning_rate * max(0.0, stress_error - 0.10)
        )

        self.disposition.causal_horizon = min(
            12.0,
            self.disposition.causal_horizon
            + 1.0
            if stress_error > 0.02 or benefit_error > 0.02
            else self.disposition.causal_horizon,
        )

        self.disposition.harm_sensitivity = clamp(
            self.disposition.harm_sensitivity
            + learning_rate * stress_error
        )

    def run_episode(
        self,
        episode_id: int,
        conditions: Dict[str, float],
    ) -> Experience:
        action = self.propose_action(conditions)
        predicted = self.predict_consequences(conditions, action)
        actual = self.observe_consequences(conditions, action)

        reflection = self.reflect(predicted, actual)
        error = reflection["prediction_error"]

        experience = Experience(
            episode_id=episode_id,
            conditions=conditions,
            intention="Respond to the present conditions with the most skillful available action.",
            action=action,
            predicted=predicted,
            actual=actual,
            prediction_error=error,  # type: ignore[arg-type]
            reflection={
                "prajna": str(reflection["prajna"]),
                "karuna": str(reflection["karuna"]),
                "upaya": str(reflection["upaya"]),
            },
        )

        self.experiences.append(experience)
        self.condition(experience)
        return experience


if __name__ == "__main__":
    learner = KarmaLedger()

    first = learner.run_episode(
        1,
        {"resource_imbalance": 0.80, "cooperation_opportunity": 0.70},
    )

    second = learner.run_episode(
        2,
        {"resource_imbalance": 0.75, "cooperation_opportunity": 0.70},
    )

    print("DIGITAL SANGHA — KARMA LEARNING EXPERIMENT")
    print("=" * 58)
    for experience in (first, second):
        print(
            f"Episode {experience.episode_id}: "
            f"sharing={experience.action['shared_resource_fraction']:.2f}, "
            f"stress={experience.actual['network_stress']:.2f}, "
            f"benefit={experience.actual['collective_benefit']:.2f}"
        )
    print("-" * 58)
    print("Persistent disposition:")
    for key, value in learner.disposition.as_dict().items():
        print(f"  {key}: {value:.3f}")
