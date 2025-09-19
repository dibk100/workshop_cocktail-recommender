import os
import json
from typing import Dict

class PromptLoader:
    def __init__(self, prompts_dir: str, config: Dict = None):
        self.prompts_dir = prompts_dir
        self.prompts: Dict[str, Dict] = {}
        self.embedding_config: Dict = {}
        self.config = config or {}
        self.load_all_prompts()
        self.load_embedding_config()

    def load_all_prompts(self):
        """prompts 디렉토리 내 JSON 파일 로딩"""
        prompt_files = [
            'base_system.json',
            'c1_visual_similarity.json',
            'c2_taste_profile.json',
            'c3_classification.json',
            'c4_recipe_ingredients.json',
            'task_classifier.json',
            'imageTotext.json',
        ]
        for filename in prompt_files:
            key = filename.replace('.json', '').lower()
            filepath = os.path.join(self.prompts_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.prompts[key] = data
            except FileNotFoundError:
                print(f"Warning: {filepath} not found. Using default prompt.")
                self.prompts[key] = {"system_prompt": "", "task_prompt": ""}
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON in {filepath}: {e}")
                self.prompts[key] = {"system_prompt": "", "task_prompt": ""}

    def load_embedding_config(self):
        """embedding_config.json 로딩"""
        filepath = os.path.join(self.prompts_dir, "embedding_config.json")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self.embedding_config = json.load(f)
        except FileNotFoundError:
            print(f"Warning: {filepath} not found. Using default embedding config.")
            self.embedding_config = {"embedding_model": "text-embedding-3-small"}
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON in {filepath}: {e}")
            self.embedding_config = {"embedding_model": "text-embedding-3-small"}

    def get_embedding_model_config(self, task_category: str = None) -> Dict:
        """태스크별 embedding 설정 반환"""
        config = self.embedding_config.copy()
        if task_category and task_category.lower() in config.get("task_specific", {}):
            task_config = config["task_specific"][task_category.lower()]
            config.update(task_config)
            print("함수 체크",config,task_config)
        return config

    def get_system_prompt(self, task_category: str) -> str:
        base_data = self.prompts.get('base_system', {})
        task_data = self.prompts.get(task_category.lower(), {})

        base_prompt = base_data.get('system_prompt', '')
        task_prompt = task_data.get('task_prompt', '')

        if task_prompt:
            return f"{base_prompt}\n\n{task_prompt}"
        return base_prompt

    def get_task_classifier_prompt(self) -> Dict:
        classifier_data = self.prompts.get('task_classifier', {})
        task_specific = self.embedding_config.get('task_specific', {}).get('task_classifier', {})

        result = {
            "system_prompt": classifier_data.get('system_prompt', 'You are a task classifier.'),
            "user_prompt": classifier_data.get('user_prompt', ''),
            "temperature": task_specific.get('temperature', self.embedding_config.get('temperature', 0.1)),
            "max_tokens": task_specific.get('max_tokens', self.embedding_config.get('max_tokens', 200)),
            "model": task_specific.get('model', self.embedding_config.get('model', 'gpt-4o-mini'))
        }
        if 'example_outputs' in classifier_data:
            result['example_outputs'] = classifier_data['example_outputs']
        return result
    
    def get_image_to_text_prompt(self) -> Dict:
        """
        imageTotext.json에 정의된 이미지→텍스트 전용 프롬프트 반환

        """
        prompt_data = self.prompts.get('imagetotext', {})
        task_specific = self.embedding_config.get('task_specific', {}).get('imageTotext', {})

        result = {
            "system_prompt": prompt_data.get('system_prompt', 'You are an image-to-text expert.'),
            "user_prompt": prompt_data.get('task_prompt', ''),
            "temperature": task_specific.get('temperature', self.embedding_config.get('temperature', 0.7)),
            "max_tokens": task_specific.get('max_tokens', self.embedding_config.get('max_tokens', 1000)),
            "model": task_specific.get('model', self.embedding_config.get('model', 'gpt-4o-mini'))
        }
        return result
