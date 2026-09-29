class Solution:

    def encode(self, strs: List[str]) -> str:
        return "##".join(strs) if strs else None
    def decode(self, s: str) -> List[str]:
        return s.split("##") if s != None else []