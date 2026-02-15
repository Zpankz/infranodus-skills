#!/usr/bin/env python3
"""
InfraNodus Workflow Analyzer
Classifies user requests and scores confidence for pattern routing.
"""

import re
from typing import Dict, List, Tuple

# Pattern keywords with weights
PATTERN_KEYWORDS = {
    "P1_deep_research": {
        "keywords": ["research", "gaps", "questions", "comprehensive", "analyze", "explore", "investigate", "deep dive", "thorough"],
        "weight": 0.85
    },
    "P2_seo": {
        "keywords": ["seo", "keyword", "search engine", "optimize", "ranking", "google", "content strategy", "serp"],
        "weight": 0.85
    },
    "P3_comparative": {
        "keywords": ["compare", "overlap", "difference", "versus", "similarities", "contrast", "between"],
        "weight": 0.80
    },
    "P4_development": {
        "keywords": ["develop", "explore", "latent", "bridge", "ideation", "brainstorm", "expand", "deepen"],
        "weight": 0.75
    },
    "P5_search_intel": {
        "keywords": ["search landscape", "market research", "what people search", "search demand", "search supply"],
        "weight": 0.85
    },
    "P6_ontology": {
        "keywords": ["ontology", "entities", "knowledge graph", "wikilinks", "relations", "extract entities"],
        "weight": 0.85
    },
    "P7_graphrag": {
        "keywords": ["retrieve", "ask graph", "knowledge base", "what does", "find in graph", "recall"],
        "weight": 0.80
    },
    "P8_simple_graph": {
        "keywords": ["analyze", "graph", "visualize", "map", "cluster", "topics"],
        "weight": 0.90
    },
    "P9_memory": {
        "keywords": ["remember", "store", "save", "recall", "memory", "memorize"],
        "weight": 0.85
    },
    "P10_cognitive": {
        "keywords": ["stuck", "brainstorm", "creative", "repetitive", "think differently", "new perspective", "blocked"],
        "weight": 0.70
    }
}

# Complexity indicators
COMPLEXITY_SIGNALS = {
    "high": ["comprehensive", "thorough", "detailed", "systematic", "multi-step", "complex", "all aspects"],
    "medium": ["analyze", "compare", "develop", "explore", "investigate"],
    "low": ["quick", "simple", "brief", "just", "basic", "fast"]
}


def _match_keyword(keyword: str, text: str) -> bool:
    """Match keyword as whole word(s) using word boundaries."""
    pattern = r'\b' + re.escape(keyword) + r'\b'
    return bool(re.search(pattern, text))


def classify_request(text: str) -> List[Tuple[str, float]]:
    """Classify request against all patterns, return scored matches."""
    text_lower = text.lower()
    scores = {}

    for pattern_id, config in PATTERN_KEYWORDS.items():
        keyword_hits = sum(1 for kw in config["keywords"] if _match_keyword(kw, text_lower))
        if keyword_hits > 0:
            # Normalize by keyword count, scale by base weight
            keyword_score = min(keyword_hits / len(config["keywords"]), 1.0) * 0.30
            base_weight = config["weight"] * 0.25
            complexity_score = _assess_complexity(text_lower) * 0.25
            artifact_score = _assess_artifact_need(text_lower, pattern_id) * 0.20
            
            total = keyword_score + base_weight + complexity_score + artifact_score
            scores[pattern_id] = min(total, 1.0)
    
    # Sort by score descending
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return ranked if ranked else [("P8_simple_graph", 0.50)]


def _assess_complexity(text: str) -> float:
    """Score complexity from text signals."""
    for level, signals in COMPLEXITY_SIGNALS.items():
        if any(_match_keyword(s, text) for s in signals):
            return {"high": 0.9, "medium": 0.5, "low": 0.2}[level]
    return 0.5


def _assess_artifact_need(text: str, _pattern: str) -> float:  # noqa: ARG001
    """Score artifact requirements based on text signals."""
    artifact_signals = {
        "save": 0.8, "export": 0.8, "document": 0.7, "report": 0.7,
        "file": 0.6, "obsidian": 0.7, "markdown": 0.6
    }
    for signal, score in artifact_signals.items():
        if _match_keyword(signal, text):
            return score
    return 0.3


def detect_content_type(text: str) -> str:
    """Detect input content type."""
    if re.search(r'https?://', text):
        return "url"
    if len(text.split('\n')) > 5 or len(text) > 500:
        return "multi_text" if '\n---\n' in text else "single_text"
    if re.search(r'\[\[.+?\]\]', text):
        return "wikilinks"
    return "topic"


def suggest_pipeline(scores: List[Tuple[str, float]], content_type: str) -> Dict:
    """Suggest optimal pipeline from classification results."""
    if not scores:
        return {"pattern": "P8_simple_graph", "pipeline": ["T01"], "confidence": 0.50}
    
    top_pattern, top_score = scores[0]
    
    pipelines = {
        "P1_deep_research": ["T01", "T06", "T08", "T11", "T12"],
        "P2_seo": ["T16", "T17", "T18", "T19"],
        "P3_comparative": ["T14", "T15", "T06", "T08"],
        "P4_development": ["T13", "T11", "T12"],
        "P5_search_intel": ["T16", "T17", "T18"],
        "P6_ontology": ["T01", "T04"],
        "P7_graphrag": ["T23", "T20", "T21"],
        "P8_simple_graph": ["T01"],
        "P9_memory": ["T04", "T05"],
        "P10_cognitive": ["cognitive_module"]
    }
    
    # Check for multi-pattern composition
    composed = None
    if len(scores) >= 2:
        second_pattern, second_score = scores[1]
        if top_score - second_score < 0.10:
            composed = {
                "type": "sequential",
                "patterns": [top_pattern, second_pattern],
                "pipeline": pipelines.get(top_pattern, []) + pipelines.get(second_pattern, [])
            }
    
    return {
        "pattern": top_pattern,
        "pipeline": pipelines.get(top_pattern, ["T01"]),
        "confidence": top_score,
        "content_type": content_type,
        "composed": composed,
        "all_scores": scores[:3]
    }


def analyze(user_request: str) -> Dict:
    """Main analysis entry point."""
    content_type = detect_content_type(user_request)
    scores = classify_request(user_request)
    suggestion = suggest_pipeline(scores, content_type)
    return suggestion
