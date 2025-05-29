from collections import defaultdict


class AdService:
    def __init__(self):
        self.data = defaultdict(list)

    def load_from_lines(self, lines):
        self.data.clear()
        for line in lines:
            try:
                if ':' not in line:
                    continue
                name, locs = line.strip().split(':', 1)
                for loc in locs.split(','):
                    clean_loc = loc.strip()
                    self.data[clean_loc].append(name)
            except Exception as e:
                print(f"→ {e}")

    def get_ads(self, location, mode='up'):
        result = set()
        location = location.strip()

        if mode == 'up':
            parts = location.strip('/').split('/')
            for i in range(len(parts), 0, -1):
                prefix = '/' + '/'.join(parts[:i])
                result.update(self.data.get(prefix, []))
        elif mode == 'down':
            for key in self.data:
                if key.startswith(location):
                    result.update(self.data[key])
        else:
            raise ValueError('Invallid mode. Use <up> or <down>')
        return sorted(result)


