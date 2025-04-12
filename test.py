# Initialize
from _databacks.quimitest import QuimiTest

dataset = QuimiTest(path='/media/quimisagi/KIOXIA/AnitaTripletsCompositedProcessed', split='all')

# Check if bns are correctly loaded
print("All bns:", dataset.bns)  # Should print ['test/0001', 'test/0002', 'train/1001', 'train/1002']

# Check __getitem__
sample = dataset[0]  # First sample
print("Sample bn:", sample['bn'])  # e.g., 'test/0001'
print("Number of images:", len(sample['images']))  # Should be 3
print("Image shape:", sample['images'][0].size)  # Should be (H, W, 3)

# Check split filtering
test_dataset = QuimiTest(path='/media/quimisagi/KIOXIA/AnitaTripletsCompositedProcessed', split='test')
print("Test bns only:", test_dataset.bns)  # Should be ['test/0001', 'test/0002']
