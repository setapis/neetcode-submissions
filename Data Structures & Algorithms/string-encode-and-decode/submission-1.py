class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []: return '@(*y3b82gf2buygf2gvefh2jehsdinjsfsdfuhsjbfudy)'
        code = '~RESPECT_SIGMA_MOMENT~'
        new_str = f'{code}'.join(strs)

        return new_str

    def decode(self, s: str) -> List[str]:
        if s == '@(*y3b82gf2buygf2gvefh2jehsdinjsfsdfuhsjbfudy)': return []
        code = '~RESPECT_SIGMA_MOMENT~'
        new = s.split('~RESPECT_SIGMA_MOMENT~')

        return new