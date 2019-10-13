const transform = (arr) => {
	console.assert(arr.length > 0)
	let finalDict = new Array(100).fill(0)
	for(let i = 0; i < arr.length; i++) {
		finalDict[arr[i].toLowerCase().charCodeAt(0) - 31] = 1
	}
	return finalDict
}
const revert = (arr) => {
	let finalDict = ""
	for(let i = 0; i < arr.length; i++) {
		if(arr[i]) {
			finalDict += String.fromCharCode(i + 31)
		}
	}
	return finalDict
}

let list = [];
// Let's quickly do an HTTP request to get our list.
let xhttp = new XMLHttpRequest(),
showAmount = 100;
xhttp.onreadystatechange = (e) => {
    if(e.target.readyState == 4 && e.target.status == 200) {
		list = e.target.responseText.split(", ")
		list = list.slice(0, 239089)
		let newArr = list.map((val) => {
			return [transform(val), val]
		}).sort((a, b) => {
			return a[0] - b[0]
		})
		// Okay, we're basically going to:
		/*
		- Alphabetize this.
		*/
		let val = ""
		// If we've already rendered this before, we set this to the exact height; until, then, we just assume it's 25 px.
		let newFiltered = list
		const reaction = (e) => {
			let start = performance.now()
			val = document.getElementById("a").value
			let fullList = []
			for(let i = 0; i < val.length; i++) {
				fullList.push(val[i].toLowerCase().charCodeAt(0) - 31)
			}
			fullList = fullList.sort()
			newFiltered = []
			// Now go through list and filter.
			for(let i = 0; i < newArr.length; i++) {
				let doWork = true
				for(let ii = 0; ii < fullList.length; ii++) {
					if(!newArr[i][0][fullList[ii]]) {
						doWork = false
					}
				}
				if(doWork) {
					if(newArr[i][1].toLowerCase().includes(val.toLowerCase())) {
						newFiltered.splice(0, 0, newArr[i][1])
					}
					else {
						newFiltered.push(newArr[i][1])
					}
				}
			}
			refresh(newFiltered.slice(0, showAmount))
			defaultTime = performance.now() - start
		}
		document.getElementById("submit").addEventListener("click", reaction)
		document.getElementById("a").addEventListener("keyup", (e) => {
			if(e.key == "Enter") {
				document.getElementById("submit").focus()
				reaction()
			}
		})
		const refresh = (options) => {
			showAmount = 100
			document.getElementById("option").innerHTML = ""
			for(let i = 0; i < options.length; i++) {
				let newElement = document.createElement("div"),
						node = document.createTextNode(options[i])
				newElement.id = options[i]
				newElement.className = "children"
				newElement.appendChild(node)
				document.getElementById("option").appendChild(newElement)
				defaultHeight = newElement.getBoundingClientRect().height
			}
		}

		window.addEventListener("scroll", () => {
			let store = window.scrollY
			if(window.scrollY + window.innerHeight > document.body.scrollHeight) {
				showAmount += 20
				if(newFiltered) {
					refresh(newFiltered.slice(0, showAmount))
					window.scrollTo(0, store)
				}
				// else {
				// 	refresh(list.slice(0, showAmount))
				// }
			}
		})
		refresh(list.slice(0, showAmount))
    }
}
xhttp.open("GET", "process")
xhttp.send()